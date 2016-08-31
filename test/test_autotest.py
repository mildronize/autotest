import unittest

from autotest import *

class TestAutotest(unittest.TestCase):

    def test_process_filename_and_package_invert(self):

        # windows
        filename = ".\\tests\\test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\test_calculator.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package_invert(filename, 'nt'))
        filename = ".\\tests\\sub\\test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package_invert(filename, 'nt'))

        filename = ".\\tests\\calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests\\calculator_test.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package_invert(filename, 'nt', False))
        filename = ".\\tests\\sub\\calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package_invert(filename, 'nt', False))

        # Unix
        filename = "./tests/test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/test_calculator.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package_invert(filename))

        filename = "./tests/sub/test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package_invert(filename))
        filename = "./tests/calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests/calculator_test.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package_invert(filename, startswith_test=False))

        filename = "./tests/sub/calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package_invert(filename, startswith_test=False))

    def test_process_filename_and_package(self):
        # windows
        filename = ".\\simple_calculator\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\test_calculator.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package(filename, 'nt'))
        filename = ".\\simple_calculator\\sub\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package(filename, 'nt'))

        filename = ".\\simple_calculator\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\calculator_test.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package(filename, 'nt', False))
        filename = ".\\simple_calculator\\sub\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package(filename, 'nt', False))

        # Unix
        filename = "./simple_calculator/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/test_calculator.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package(filename))
        filename = "./simple_calculator/sub/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package(filename))
        filename = "./simple_calculator/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/calculator_test.py",
                "package": "simple_calculator.calculator"
            }, process_filename_and_package(filename, startswith_test=False))
        filename = "./simple_calculator/sub/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, process_filename_and_package(filename, startswith_test=False))

    def test_get_filename_and_package(self):
        assert True
