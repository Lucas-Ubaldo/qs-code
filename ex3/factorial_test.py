import unittest
from factorial import factorial

class FactorialTest(unittest.TestCase):
    def test_factorial_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_one(self):
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_positive(self):
        result = factorial(5)
        self.assertEqual(result, 120)

    def test_factorial_large_number(self):
        result = factorial(10)
        self.assertEqual(result, 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_float(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_string(self):
        with self.assertRaises(TypeError):
            factorial("10")

if __name__ == '__main__':
    unittest.main()