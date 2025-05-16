import unittest
from app import add

class TestMathOp(unittest.TestCase):
    def test_add(self):
        result = add(2, 4)
        self.assertEqual(result, 6)
if __name__ == "__main__":
    unittest.main()
