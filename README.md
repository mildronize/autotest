# auto-test
Auto test script ( watchdog + nose ) for TDD ( with test )

## Requirements
see in `requirements_dev.txt`

## Feature
- Watch a file and if the file is modified, the test will start. 
- Support Windows and Unix path

## Develpment
1. Clone this project
2. Create and activate a python virtual environment
3. Install requirements by: `pip install -r requirements_dev.txt`
4. Test by: `make test`