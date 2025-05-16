import unittest
class Calculator:
    def add(self, a, b):
        return a + b
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
if __name__ == "__main__":
    unittest.main()