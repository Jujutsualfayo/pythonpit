import unittest
from app import add, subtract, multiply, division

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 7), 10)
        self.assertEqual(add(-3, 5), 2)

    def test_subtract(self):
        self.assertEqual(subtract(7, 2), 5)
        self.assertEqual(subtract(12, 3), 9)
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(2, -3), -6)
    def test_division(self):
        self.assertEqual(division(6, 2), 3)
        self.assertAlmostEqual(division(7, 3), 2.3333, places=4)
    def test_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

if __name__ == "__main__":
    unittest.main()


