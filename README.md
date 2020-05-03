<div align="center">

# Diff

Display a diff between two files in HTML.

[![Build Status](https://travis-ci.com/Justintime50/diff.svg?branch=master)](https://travis-ci.com/Justintime50/diff)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

## Install

```bash
pip install -r requirements.txt
```

## Usage

1) Place the contents of the older file in `f1.html` and the contents of the newer file in `f2.html`. **Just think "New in 2".**
2) Run the script and it will generate an HTML file.
3) Open the HTML file in a browser and view the diff.

```bash
python diff.py > diff.html

open diff.html
```
