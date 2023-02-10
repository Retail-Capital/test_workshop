## Overview

This repo is all about getting familiar with testing. In particular, it will be used to illustrate the basics of automated testing, some principles of unit testings and exposure to TDD.

## Installation

1. `pipenv install`

That's it  :-D  Woohoo. Typically these packages would be dev packages but for the sake of this exercises, they're in the main package listing.

Components worth noting:

- pytest is the testing framework that we will be using
- pytest-sugar is a way of presenting the output that make things much nicer to see

## Running Tests

1. `pipenv run pytest tests/unit/app/bank_account_tests.py`


## Pytest Cheatsheet

Run pytest on all tests matching a particular string: -k [string]
Example: `pipenv run pytest -k 'absolute'` will run all tests with the word `absolute` in the test name
