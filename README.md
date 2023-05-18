# setup-jython

[![Jython tests](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml)

This action provides the following functionality for GitHub Actions users:

- Installing a version of Jython and adding it to `PATH`
- Customizing the installation path

## Basic usage

```yml
steps:
- uses: actions/checkout@v3

- name: Install Jython
  uses: LukeSavefrogs/setup-jython@v1
  with:
    jython-version: '2.5.2'
    installation-path: '~/jython/'   # Default

- run: jython -c 'import sys, os; print(os.name, sys.version)';
```

## Supported versions

This action supports all versions currently listed on the official repositories:

- [SourceForge](https://sourceforge.net/projects/jython/files/jython/) (`2.0` - `2.5.2`)
- [Maven](https://search.maven.org/artifact/org.python/jython-installer) (`2.5.3-rc1` - `2.7.3`)

> **NOTE**
>
> As of `v1`, this action does not support Jython 2.0 and 2.1!
