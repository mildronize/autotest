# auto-test
[![Build Status](https://travis-ci.org/mildronize/autotest.svg?branch=master)](https://travis-ci.org/mildronize/autotest)
[![Coverage Status](https://coveralls.io/repos/github/mildronize/auto-test/badge.svg?branch=master)](https://coveralls.io/github/mildronize/auto-test?branch=master) 
[![Code Health](https://landscape.io/github/mildronize/autotest/master/landscape.svg?style=flat)](https://landscape.io/github/mildronize/autotest/master)

Auto test script ( watchdog + nose ) for TDD ( with test )

## Requirements
- Support Python version:  2.7, 3.3, 3.4, 3.5, 3.5-dev, nightly
- see in `requirements.txt`

## Feature
- Watch a file and if the file is modified, the test will start. 
- Support Windows and Unix path

## Development
1. Clone this project
2. Create and activate a python virtual environment
3. Install requirements by: `pip install -r requirements.txt`
4. Test by: `make test`

## Todo
- [x] Build on Travis CI
- [ ] Use tox test runner
