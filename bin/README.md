# Resources list

The file `resources.json` contains an array of all the available Jython installers that will be used by the action.

```jsonc
[
    /* ... */
    {
        "version": "2.5.2",
        "resource_urls": {
            "official": "https://downloads.sourceforge.net/project/jython/jython/2.5.2/jython_installer-2.5.2.jar",
            "mirrored": null
        },
        "modified_on": "2011-03-03"
    },
    /* ... */
]
```

## Sources

The binaries are gathered from all the **3 official sources**:

- [Sourceforge (_dev_)](https://sourceforge.net/projects/jython/files/jython-dev/)
- [Sourceforge (_stable_)](https://sourceforge.net/projects/jython/files/jython/)
- [Maven (_dev_ + _stable_)](https://central.sonatype.com/artifact/org.python/jython-installer/2.7.3) (_the old website is available [here](https://search.maven.org/artifact/org.python/jython-installer)_)
