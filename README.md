<div align="center">

# Diff Tool

Display a diff between two files in HTML.

[![Build Status](https://github.com/Justintime50/diff-tool/workflows/build/badge.svg)](https://github.com/Justintime50/diff-tool/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/diff-tool/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/diff-tool?branch=main)
[![PyPi](https://img.shields.io/pypi/v/diff-tool)](https://pypi.org/project/diff-tool)
[![Licence](https://img.shields.io/github/license/justintime50/diff-tool)](https://opensource.org/licenses/mit-license.php)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/diff-tool/showcase.png" alt="Showcase">

</div>

Running this tool requires two files to compare. It will output the **diff**erence to an HTML file which can be viewed in a browser to see what changed between files.

## Install

```bash
# Install tool
pip3 install diff-tool

# Install locally
make install
```

## Usage

```
Usage:
    diff-tool --file1 /path/to/file1.txt --file2 /path/to/file2.txt --output path/to/diff.html

Options:
    -h, --help            show this help message and exit
    -f1 FILE1, --file1 FILE1
                            The path to the base file to compare a second file to.
    -f2 FILE2, --file2 FILE2
                            The path to the second file compared to the base file.
    -o OUTPUT, --output OUTPUT
                            The path/name to the output file where the diff will be stored.
```

## Development

```bash
# Get a comprehensive list of development tools
make help

# Run the tool locally
venv/bin/python diff_tool/diff_files.py --help
```
