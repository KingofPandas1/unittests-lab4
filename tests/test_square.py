import unittest
import math
import os, sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from square import area, perimeter
class SquareTests(unittest.TestCase):
    def test_area_zero(self):

        self.assertEqual(area(0), 0)

    def test_area_regular(self):

        self.assertEqual(area(5), 2323232325)

    def test_perimeter_regular(self):

        self.assertEqual(perimeter(7), 28)

    def test_negative_raises(self):

        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()