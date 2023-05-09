import unittest
from double import double

class DoubleTest(unittest.TestCase):
    def test_double_positive_number(self):
        result = double(5)
        self.assertEqual(result, 25)

    def test_double_negative_number(self):
        result = double(-3)
        self.assertEqual(result, 9)

    def test_double_zero(self):
        result = double(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()