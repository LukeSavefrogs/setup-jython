# setup-jython

[![Jython tests](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml)
[![Source download URLs status](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-urls.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-urls.yml)

This action provides the following functionalities for GitHub Actions users:

- Installing a version of Jython and adding it to `PATH`
- Customizing the installation path

## Basic usage

```yml
steps:
- name: Install Jython
  uses: LukeSavefrogs/setup-jython@v3
  with:
    jython-version: '2.5.2'

- run: jython -c 'import sys, os; print(os.name, sys.version)';
```

## Inputs

### `jython-version`

Specify the version of Jython to install. The value must be one of the versions listed in the [Supported versions](#supported-versions) section.

<table>
    <thead align=center>
        <tr>
            <th>Type</th>
            <th>Required</th>
            <th>Default</th>
        </tr>
    </thead>
    <tbody align=center>
        <tr>
            <td>string</td>
            <td>yes</td>
            <td>-</td>
        </tr>
    </tbody>
</table>

### `installation-path`

Specify the path where Jython will be installed. Please note that this is usually not needed, since the binaries are always added to `PATH` anyway.

<table>
    <thead align=center>
        <tr>
            <th>Type</th>
            <th>Required</th>
            <th>Default</th>
        </tr>
    </thead>
    <tbody align=center>
        <tr>
            <td>string</td>
            <td>no</td>
            <td><code>~/jython/</code></td>
        </tr>
    </tbody>
</table>

## Supported versions

This action supports all versions (_both stable and development releases_) currently listed on the official repositories:

- [SourceForge - Stable](https://sourceforge.net/projects/jython/files/jython/) (`2.0` - `2.5.2`)
- [SourceForge - Development](https://sourceforge.net/projects/jython/files/jython-dev/) (`2.5a1` - `2.7.0a2`)
- [Maven](https://search.maven.org/artifact/org.python/jython-installer) (`2.5.3-rc1` - `2.7.3`)

> ⚠️ **WARNING** ⚠️
>
> As of **`v3`**, Jython versions **2.0**/**2.1** **work only on `windows-*` runners**!
>
> See issue [#1](https://github.com/LukeSavefrogs/setup-jython/issues/1) for more info..
