# CHANGELOG

## v2.0.0 (2021-02-06)

* Renamed `diff-tool` from `diff` to match published name and avoid conflict with potential other `diff` tools
* Changed all classmethods to staticmethods
* Switched from Travis CI to GitHub Actions

## v1.3.1 (2020-08-26)

* Simplified unit tests

## v1.3.0 (2020-08-20)

* Overhauled testing suite (less exclusions, more robust tests)

## v1.2.1 (2020-08-14)

* Fixed the entry point for the script (pip installs work again)

## v1.2.0 (2020-08-12)

* Various bug fixes and code refactors
* Mocked all tests
* Added pytest and coveralls

## v1.1.0 (2020-08-12)

* Added automated releases via Travis
* Updated README badges
* Added Makefile
* Added unit tests
* Cleaned up code to be more pythonic
* Switched from Pylint to Flake8

## v1.0.1 (2020-07-16)

* Script now outputs the data directly to an HTML file in-code instead of requiring this on the command line.
* Added a print statement when the script is complete.

## v1.0.0 (2020-07-16)

* Added argparse to take file paths as params
* Moved to module, added `setup.py`, published to Pypi
* Cleaned up project

## v0.1.0 (2019)

* Initial project, compare two files in HTML. Hard programmed filenames, no module.
