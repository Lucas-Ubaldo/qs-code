import unittest
from calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):

    def test_soma_1_2(self):
         self.assertEqual(
             Calculadora.somar(1, 2), 3)

    def test_soma_10_1(self):
         self.assertEqual(
             Calculadora.somar(10, 1), 11)

    def test_soma_1_99(self):
         self.assertEqual(
             Calculadora.somar(1, 99), 100)



    def test_subtracao_2_1(self):
         self.assertEqual(
             Calculadora.subtrair(2, 1), 1)

    