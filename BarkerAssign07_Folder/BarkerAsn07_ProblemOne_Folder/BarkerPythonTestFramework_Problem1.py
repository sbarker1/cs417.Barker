# Samuel Barker
# sbarker1@my.athens.edu
# Assignment 7, Problem 1 Test Framework source

# Reference Citations:
# [1] https://docs.python.org/3/library/unittest.html
# [2] https://www.browserstack.com/guide/unit-testing-python

import unittest # [1]
import subprocess

class TestGeometricModelingSystem(unittest.TestCase):
    def run_command(self, command):  # [2]
        process = subprocess.Popen(
            "python BarkerAsn07_Problem1.py",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            shell=True,
        )
        output, _ = process.communicate(input=command)
        return output

# Implemented the same tests as the test script screenshots found in my document. 

    def test_create_square(self):  # [1]
        command = "C 1 17\nP\nX"
        output = self.run_command(command)
        self.assertIn("(1,0,0,17)", output)

    def test_move_square(self):
        command = "C 1 17\nM 1 3 4\nP\nX"
        output = self.run_command(command)
        self.assertIn("(1,3,4,17)", output)

    def test_scale_square(self):
        command = "C 1 17\nS 1 2\nP\nX"
        output = self.run_command(command)
        self.assertIn("(1,0,0,34.0)", output)

    def test_undo_command(self):
        command = "C 1 17\nM 1 3 4\nS 1 2\nP\nU\nP\nX"
        output = self.run_command(command)
        self.assertIn("(1,3,4,17)", output)

    def test_redo_command(self):
        command = "C 1 17\nM 1 3 4\nS 1 2\nP\nU\nP\nR\nP\nX"
        output = self.run_command(command)
        self.assertIn("(1,3,4,34.0)", output)

if __name__ == "__main__":
    unittest.main()

# Output when run: Ran 5 tests in ____s OK