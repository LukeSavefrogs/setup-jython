# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.0] - 2023-06-08

### Breaking changes

- Renamed action output `jython-download-url` to `download-url`

### Added

- Support for Jython 2.0 and 2.1 (_only on `windows-*` runners_, see [#1](https://github.com/LukeSavefrogs/setup-jython/issues/1))
- Exit with error when provided Jython version does not exist

### Fixed

- `download-url` description now do not have a placeholder text but actually holds meaningful info
