# Leetcode solutions in Python

[![Build Status](https://travis-ci.org/huajianmao/pyleet.svg?branch=master)](https://travis-ci.org/huajianmao/pyleet)
[![codecov](https://codecov.io/gh/huajianmao/pyleet/branch/master/graph/badge.svg)](https://codecov.io/gh/huajianmao/pyleet)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8115b530daf64bdeb92b8125b627102c)](https://www.codacy.com/manual/huajianmao/pyleet?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=huajianmao/pyleet&amp;utm_campaign=Badge_Grade)

![Language](https://img.shields.io/badge/Language-Python3-success.svg?logo=Python&logoColor=yellow)
![Update](https://img.shields.io/badge/Update-Daily-success.svg)
![Test Cases](https://img.shields.io/badge/Tests-117-success.svg)
![Progress](https://img.shields.io/badge/Progress-34%2F1172-critical.svg)

## Introduction
Solutions for Leetcode problems in Python3.

## Environment
This project is coded in Python 3 and managed with Makefile.

The test cases uses the default `pytest` framework.

## Code Layout
 - `src/solutions`: will holds all your solutions.
   The code are in the same code format as the leetcode requires,
   so when you passed your own unit test cases, it can be directly copied and pasted on the leetcode OJ input box.
   It also holds the test cases for the solution.

 - `src/utils`: contains some of the utilities for the Leetcode solutions.

 - `Makefile`: You may run `make init` first to run the dependencies, and test your solutions with `make test`.
   The `make check` will check the code style first then run `make test`.
   It will run `make check` by default.

 
<details><summary>Source Code Layout</summary>
<p>

``` shell
.
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── solutions
│   │   ├── __init__.py
│   │   ├── a0000blank.py
│   │   └── a0001twosum.py
│   └── utils
│       └── __init__.py
├── test_requirements.txt
└── tests
    ├── __init__.py
    ├── test_a0000blank.py
    └── test_a0001twosum.py
```
</p>
</details>

## How to use this repo

 1. Clone this project `git clone https://github.com/huajianmao/pyleet`

 2. Run `make init` to install the dependencies

 3. Choose a problem and create the `a00xxtitle.py` in the `src/solutions`, and write your solution in this file.

 4. Create a test file `test_a00xxtitle.py` in the `tests`, and write your test cases in this file.

 5. Test your solution with `make test`.

 6. Before you commit code, it would be better to run `make check` to check the code style.
