#!/usr/bin/python3
import unittest

class TestDemo(unittest.TestCase):
    def test_noting(self):
        print("testing nothing")
        self.assertEqual(None, None)

    def test_oneplusone(self):
        print("testing one plus one")
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
