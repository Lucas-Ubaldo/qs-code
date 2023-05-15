import unittest
from calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):

    def test_soma_1_1(self):
         self.assertEqual(
             Calculadora.somar(1, 1), 2)