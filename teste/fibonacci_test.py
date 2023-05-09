import unittest
from math_samples import MathSamples

class FibonacciTest(unittest.TestCase):

    def teste_fib01(self):
        """Testando caso para entrada = 0"""
        self.assertEqual(
            MathSamples.fibonacci(0),
            0

        )
    
    def test_fib02(self):
        """Testando caso para entrada = 1"""
        self.assertEqual(
            MathSamples.fibonacci(1),
            1
        )   
    
    def test_fib03(self):
        """Testando caso para entrada = 2"""
        self.assertEqual(
            MathSamples.fibonacci(2),
            1
        )   

    def test_fib04(self):
        """Testando caso para entrada = 3"""
        self.assertEqual(
            MathSamples.fibonacci(3), 
            2)

    def test_fib05(self):
        """Testando caso para entrada = 4"""
        self.assertEqual(
            MathSamples.fibonacci(4), 
            3)

    def test_fib06(self):
        """Testando caso para entrada = 5"""
        self.assertEqual(
            MathSamples.fibonacci(5), 
            5)

    def test_fib07(self):
        """Testando caso para entrada = 6"""
        self.assertEqual(
            MathSamples.fibonacci(6), 
            8)
    