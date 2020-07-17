<div align="center">

# Diff

Display a diff between two files in HTML.

[![Build Status](https://travis-ci.com/Justintime50/diff.svg?branch=master)](https://travis-ci.com/Justintime50/diff)
[![Pypi](https://img.shields.io/pypi/v/diff-tool)](https://pypi.org/project/diff-tool)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

## Install

```bash
pip3 install diff-tool
```

## Usage

Running this tool requires two files to compare and will output the **diff**erence to `diff.html`.

```
Usage:
    diff-tool -f1 /path/to/file1.txt -f2 /path/to/file2.txt

Options:
    -h, --help                show this help message and exit
    -f1 FILE1, --file1 FILE1  The base file to compare a second file to.
    -f2 FILE2, --file2 FILE2  The second file compared to the base first file.
```

## Development

Install project with dev depencencies:

```bash
pip3 install -e ."[dev]"
```

Lint the project:

```bash
pylint diff/*.py
```
