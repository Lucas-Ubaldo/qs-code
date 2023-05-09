import unittest
from power import power

class PowerTest(unittest.TestCase):
    def test_power_positive_numbers(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

    def test_power_negative_base(self):
        result = power(-2, 4)
        self.assertEqual(result, 16)

    def test_power_zero_exponent(self):
        result = power(5, 0)
        self.assertEqual(result, 1)

    def test_power_base_zero(self):
        result = power(0, 5)
        self.assertEqual(result, 0)

    def test_power_negative_exponent(self):
        result = power(4, -2)
        self.assertEqual(result, 0.0625)

if __name__ == '__main__':
    unittest.main()