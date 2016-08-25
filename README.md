# auto-test
[![Build Status](https://travis-ci.org/mildronize/auto-test.svg?branch=master)](https://travis-ci.org/mildronize/auto-test)

Auto test script ( watchdog + nose ) for TDD ( with test )

## Requirements
- Support Python version:  2.7, 3.3, 3.4, 3.5, 3.5-dev, nightly
- see in `requirements.txt`

## Feature
- Watch a file and if the file is modified, the test will start. 
- Support Windows and Unix path

## Develpment
1. Clone this project
2. Create and activate a python virtual environment
3. Install requirements by: `pip install -r requirements.txt`
4. Test by: `make test`

## Todo
- [x] Build on Travis CI
- [ ] Use tox test runner