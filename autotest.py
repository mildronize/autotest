#!/usr/bin/env python

import os
import ntpath
import posixpath


class PathProcessor:

    def __init__(self, unittest_dir, package_name, startswith_test):
        self.unittest_dir = unittest_dir
        self.package_name = package_name
        self.startswith_test = startswith_test

    def process_filename_and_package_invert(self, file_path, os_name=None, startswith_test=True):
        if os_name == 'nt':
            seperater = "\\"
        else:
            seperater = "/"
        if startswith_test:
            test_style = "test_"
        else:
            test_style = "_test"
        package = file_path.replace(self.unittest_dir+seperater, "").replace(".py", "")[2:]
        # print(package)
        package = package.replace(seperater, ".").replace(test_style, "")
        package = "{}.{}".format(self.package_name , package)
        # print(package) print(os.path.abspath(file_path))
        test_file_path = file_path[2:]
        return {
            "test_file_path": test_file_path,
            "package": package
        }

    def process_filename_and_package(self, file_path, os_name=None, startswith_test=True):
        if os_name == 'nt':
            seperater = "\\"
        else:
            seperater = "/"

        # file_path == "./simple_calculator/sub/calculator.py"
        removed_head_tail = file_path[2:-3]
        # removed_head_tail == "simple_calculator/sub/calculator"
        package = removed_head_tail.replace(seperater, ".")
        # package == "simple_calculator.sub.calculator"

        # basename = os.path.basename(file_path)
        if os_name == 'nt':
            basename = ntpath.basename(file_path)
        else:
            basename = posixpath.basename(file_path)
        # basename == "calculator.py"
        prefix_path = file_path[2:].replace(basename, "")[:-1].replace(file_path.split(seperater)[1], "")
        # prefix_path == "/sub"
        if startswith_test:
            test_basename = "test_{}".format(basename)
        else:
            test_basename = "{}_test.py".format(basename.replace(".py", ""))
        test_file_path = "{}{}{}{}".format(self.unittest_dir, prefix_path, seperater, test_basename)
        return {
            "package": package,
            "test_file_path": test_file_path
        }

    def get_filename_and_package(self, file_path, os_name, startswith_test):
        basename = os.path.basename(file_path)
        if basename.startswith("test_") and basename.endswith(".py"):
            return self.process_filename_and_package_invert(file_path, os_name, startswith_test)
        if basename.endswith("_test.py"):
            return self.process_filename_and_package_invert(file_path, os_name, startswith_test)
        else:
            return self.process_filename_and_package(file_path, os_name, startswith_test)

    def when_file_changed(self, filename):
        os.system('cls' if os.name == 'nt' else 'clear')
        args = self.get_filename_and_package(filename, os.name,
                self.startswith_test)
        nose = "nosetests"
        options = "--rednose --with-coverage --cover-erase " \
            "--cover-package={package} -v {test_file_path}".format(**args)
        # -v verbose show a list of tests
        cmd = nose + " " + options
        print(cmd)
        os.system(cmd)


