.PHONY: test

# CONFIG
PACKAGE_NAME := auto_test 

test: ## Test all codes with coverage
	nosetests --rednose --with-coverage --cover-erase --cover-package=$(PACKAGE_NAME) -v test/test_auto_test.py