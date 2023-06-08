# setup-jython

[![Jython tests](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml)
[![Source download URLs status](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-urls.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-urls.yml)

This action provides the following functionality for GitHub Actions users:

- Installing a version of Jython and adding it to `PATH`
- Customizing the installation path

## Basic usage

```yml
steps:
- uses: actions/checkout@v3

- name: Install Jython
  uses: LukeSavefrogs/setup-jython@v3
  with:
    jython-version: '2.5.2'
    installation-path: '~/jython/'   # Default

- run: jython -c 'import sys, os; print(os.name, sys.version)';
```

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
