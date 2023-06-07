from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

import requests

color_green = '\033[92m'
color_red = '\033[91m'
color_reset = '\033[0m'

class JSONWithCommentsDecoder(json.JSONDecoder):
    def __init__(self, **kw):
        super().__init__(**kw)

    def decode(self, s: str) -> Any:
        s = '\n'.join(l for l in s.split('\n') if not l.lstrip(' ').startswith('//'))
        return super().decode(s)

if __name__ == '__main__':
    check_success = True
    with open('bin/resources.json', 'r') as f:
        raw_resources = json.load(f, cls=JSONWithCommentsDecoder)

    # Order the resources by date
    resources = sorted(raw_resources, key=lambda r: datetime.strptime(r["modified_on"], "%Y-%m-%d"))

    if resources != raw_resources:
        print("Resources were not ordered by date, dumping them back to the file...")
        # Write the resources back to the file, to keep the order
        with open('bin/resources.json', 'w') as f:
            json.dump(resources, f, indent=4)
    
    for resource in resources:
        if not resource['resource_urls']["official"]:
            continue

        print(f"--------------- {resource['version']} ---------------")
        print("Official: ", end="", flush=True)

        response = requests.head(resource['resource_urls']["official"], allow_redirects=True)
        content_type = response.headers.get('Content-Type', "")

        if resource['resource_urls']["mirrored"] is not None:
            binary_path = Path(resource['resource_urls']["mirrored"]).resolve()
        else:
            binary_path = None

        remote_online = True

        if response.status_code != 200:
            print(f"{color_red}KO{color_reset} (Jython version {resource['version']} not available online)")
            remote_online = False
            check_success = False

        if content_type not in ['application/java-archive', 'application/octet-stream']:
            print(f"{color_red}KO{color_reset} (Unknown content type {content_type} for Jython version {resource['version']})")
            remote_online = False
            check_success = False

        if remote_online:
            print(f"{color_green}OK{color_reset}", flush=True)

        if binary_path is not None:
            print("Mirrored: ", end="", flush=True)
            if binary_path.exists():
                print(f"{color_green}OK{color_reset}", flush=True)
                check_success = True

            elif remote_online:
                try:
                    with requests.get(resource['resource_urls']["official"], allow_redirects=True, stream=True) as r:
                        r.raise_for_status()
                        
                        file_extension = resource['resource_urls']["official"].split('.')[-1]
                        with open(resource['resource_urls']["mirrored"], 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192): 
                                f.write(chunk)
                except Exception as e:
                    print(f"{color_red}KO{color_reset} (cannot download due to {e})", flush=True)
                    check_success = False
                else:
                    print(f"{color_green}OK{color_reset} (version {resource['version']} downloaded)")
                    check_success = True
            else:
                print(f"{color_red}KO{color_reset} (cannot download due to resource not available online)", flush=True)
                check_success = False
        print("")

    sys.exit(0 if check_success else 1)