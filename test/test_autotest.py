import unittest

from autotest import PathProcessor


class TestProcessFilenameAndPackageInvert(unittest.TestCase):

    def setUp(self):
        self.pp = PathProcessor("tests", "simple_calculator", True)

    def test_process_filename_and_package_invert_windows_1(self):
        filename = ".\\tests\\test_calculator.py"
        self.assertEqual({
                "test_file_path": "tests\\test_calculator.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package_invert(filename, 'nt'))

    def test_process_filename_and_package_invert_windows_2(self):
        filename = ".\\tests\\sub\\test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package_invert(filename, 'nt'))

    def test_process_filename_and_package_invert_windows_3(self):
        filename = ".\\tests\\calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests\\calculator_test.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package_invert(filename, 'nt', False))

    def test_process_filename_and_package_invert_windows_4(self):
        filename = ".\\tests\\sub\\calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package_invert(filename, 'nt', False))

    def test_process_filename_and_package_invert_unix_1(self):
        filename = "./tests/test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/test_calculator.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package_invert(filename))

    def test_process_filename_and_package_invert_unix_2(self):
        filename = "./tests/sub/test_calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package_invert(filename))

    def test_process_filename_and_package_invert_unix_3(self):
        filename = "./tests/calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests/calculator_test.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package_invert(filename, startswith_test=False))

    def test_process_filename_and_package_invert_unix_4(self):
        filename = "./tests/sub/calculator_test.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package_invert(filename, startswith_test=False))

class TestProcessFilenameAndPackage(unittest.TestCase):

    def setUp(self):
        self.pp = PathProcessor("tests", "simple_calculator", True)

    def test_process_filename_and_package_windows_1(self):
        filename = ".\\simple_calculator\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\test_calculator.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package(filename, 'nt'))

    def test_process_filename_and_package_windows_2(self):
        filename = ".\\simple_calculator\\sub\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package(filename, 'nt'))

    def test_process_filename_and_package_windows_3(self):
        filename = ".\\simple_calculator\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\calculator_test.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package(filename, 'nt', False))

    def test_process_filename_and_package_windows_4(self):
        filename = ".\\simple_calculator\\sub\\calculator.py"
        self.assertEqual( {
                "test_file_path": "tests\\sub\\calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package(filename, 'nt', False))

    def test_process_filename_and_package_unix_1(self):
        filename = "./simple_calculator/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/test_calculator.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package(filename))

    def test_process_filename_and_package_unix_2(self):
        filename = "./simple_calculator/sub/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/test_calculator.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package(filename))

    def test_process_filename_and_package_unix_3(self):
        filename = "./simple_calculator/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/calculator_test.py",
                "package": "simple_calculator.calculator"
            }, self.pp.process_filename_and_package(filename, startswith_test=False))

    def test_process_filename_and_package_unix_4(self):
        filename = "./simple_calculator/sub/calculator.py"
        self.assertEqual( {
                "test_file_path": "tests/sub/calculator_test.py",
                "package": "simple_calculator.sub.calculator"
            }, self.pp.process_filename_and_package(filename, startswith_test=False))

