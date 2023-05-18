# setup-jython

[![Jython tests](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml/badge.svg)](https://github.com/LukeSavefrogs/setup-jython/actions/workflows/test-action.yml)

This action provides the following functionality for GitHub Actions users:

- Installing a version of Jython and adding it to `PATH`

## Basic usage

```yml
steps:
- uses: actions/checkout@v3

- name: Install Jython
  uses: actions/setup-jython@v1
  with:
    jython-version: '2.5.2'

- run: jython -c 'import sys, os; print(os.name, sys.version)';
```
