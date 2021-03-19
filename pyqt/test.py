#!/usr/bin/python3
import unittest
import os


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # run tests
    loader = unittest.TestLoader()
    start_dir = dname + "/tests"
    tests = loader.discover(start_dir)
    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)
