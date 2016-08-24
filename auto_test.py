#!/usr/bin/env python

import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# STYLE="startswith_test"
# STYLE="endswith_test"
UNITEST_DIR = "tests" # ending without /
PACKAGE_NAME = "simple_calculator"
STARTSWITH_TEST = True

def process_filename_and_package_invert(file_path, os_name=None, startswith_test=True):
    if os_name == 'nt':
        seperater = "\\"
    else:
        seperater = "/"
    if startswith_test:
        test_style = "test_"
    else:
        test_style = "_test"
    package = file_path.replace( UNITEST_DIR+seperater, "").replace(".py", "")[2:]
    print(package)
    package = package.replace(seperater, ".").replace(test_style, "")
    package = "{}.{}".format(PACKAGE_NAME, package)
    print(package)
    print(os.path.abspath(file_path))
    test_file_path = file_path[2:]
    return {
        "test_file_path": test_file_path,
        "package": package
    }

def process_filename_and_package(file_path, os_name=None, startswith_test=True):
    if os_name == 'nt':
        seperater = "\\"
    else:
        seperater = "/"

    # file_path == "./simple_calculator/sub/calculator.py"
    removed_head_tail = file_path[2:-3]
    # removed_head_tail == "simple_calculator/sub/calculator"
    package = removed_head_tail.replace(seperater, ".")
    # package == "simple_calculator.sub.calculator"

    basename = os.path.basename(file_path)
    # basename == "calculator.py"
    prefix_path = file_path[2:].replace(basename, "")[:-1].replace(file_path.split(seperater)[1], "")
    print(prefix_path)
    # prefix_path == "/sub"
    if startswith_test:
        test_basename = "test_{}".format(basename)
    else:
        test_basename = "{}_test.py".format(basename.replace(".py",""))
    test_file_path = "{}{}{}{}".format(UNITEST_DIR, prefix_path, seperater, test_basename)
    return {
        "package": package,
        "test_file_path": test_file_path
    }

def get_filename_and_package(file_path, os_name, startswith_test):
    basename = os.path.basename(file_path)
    if basename.startswith("test_") and basename.endswith(".py"):
        return process_filename_and_package_invert(file_path, os_name, startswith_test)
    if basename.endswith("_test.py"):
        return process_filename_and_package_invert(file_path, os_name, startswith_test)
    else:
        return process_filename_and_package(file_path, os_name, startswith_test)

def when_file_changed(filename):
    # cls()
    # filename = os.path.abspath(filename)
    args = get_filename_and_package(filename, os.name, STARTSWITH_TEST)
    nose = "nosetests"
    options = "--rednose --with-coverage --cover-erase " \
        "--cover-package={package} -v {test_file_path}".format(**args)
    # -v verbose show a list of tests
    cmd = nose + " " + options
    print(cmd)
    os.system(cmd)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ModifiedHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def on_created(self, event):
        when_file_changed(event.src_path)

    def on_any_event(self, event):
        print(event)

    def on_modified(self, event):
        when_file_changed(event.src_path)

if __name__ == '__main__':
    args = sys.argv[1:]
    event_handler = ModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler,
                      path=args[1] if args else '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
