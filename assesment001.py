# rectangle

class Rectangle:
    def __init__(self, width: float, length: float):
        self.width = float(width)
        self.length = float(length)

    def get_area(self) -> float:
        return self.width * self.length

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def vertical_orientation(self) -> bool:
        return self.width > self.length

# test_rectangle

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_square_rectangle(self):
        r = Rectangle(5.0, 5.0)
        self.assertEqual(r.get_area(), 25.0)
        self.assertEqual(r.get_perimeter(), 20.0)
        self.assertFalse(r.vertical_orientation())

    def test_vertical_rectangle(self):
        r = Rectangle(7.0, 3.0)
        self.assertEqual(r.get_area(), 21.0)
        self.assertEqual(r.get_perimeter(), 20.0)
        self.assertTrue(r.vertical_orientation())

    def test_horizontal_rectangle(self):
        r = Rectangle(4.0, 8.0)
        self.assertEqual(r.get_area(), 32.0)
        self.assertEqual(r.get_perimeter(), 24.0)
        self.assertFalse(r.vertical_orientation())

    def test_zero_dimensions(self):
        r = Rectangle(0.0, 0.0)
        self.assertEqual(r.get_area(), 0.0)
        self.assertEqual(r.get_perimeter(), 0.0)
        self.assertFalse(r.vertical_orientation())

if __name__ == '__main__':
    unittest.main()
