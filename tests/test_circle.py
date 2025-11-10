import unittest
import math
import os, sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from circle import area, perimeter


class CircleTests(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0.0)

    def test_area_regular(self):
        self.assertAlmostEqual(area(3), math.pi * 9, places=7)

    def test_perimeter_regular(self):
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5, places=7)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()


"""
python -m unittest tests/test_circle.py -v
"""