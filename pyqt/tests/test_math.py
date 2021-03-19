#!/usr/bin/python3
import unittest

class AVerySmartClass:
    def __init__(self):
        pass

    def compute_meaning_of_life(self):
        return 42

class TestMath(unittest.TestCase):
    def test_dot1_plus_dot2(self):
        print("testing for 0.1 + 0.2 = 0.3")
        print("Oops, something went wrong! Do you know why?")
        self.assertEqual(0.1 + 0.2, 0.3)

    def test_what_is_meaning_of_life(self):
        print("testing for meaning of life")
        a_very_smart_object = AVerySmartClass()
        self.assertEqual(a_very_smart_object.compute_meaning_of_life(), 42)


if __name__ == "__main__":
    unittest.main()
