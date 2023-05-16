import unittest
from calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):

    #Adição
    def test_soma_1_2(self):
         self.assertEqual(
             Calculadora.somar(1, 2), 3)

    def test_soma_10_1(self):
         self.assertEqual(
             Calculadora.somar(10, 1), 11)

    def test_soma_1_99(self):
         self.assertEqual(
             Calculadora.somar(1, 99), 100)

    #subtração
    def test_subtracao_2_1(self):
         self.assertEqual(
             Calculadora.subtrair(2, 1), 1)

    def test_subtracao_1_2(self):
         self.assertEqual(
             Calculadora.subtrair(1, 2), -1)

    def test_subtracao_1_2(self):
         self.assertEqual(
             Calculadora.subtrair(0, 0), 0)


    #multiplicação
    def test_multiplicacao_10_1(self):
         self.assertEqual(
             Calculadora.multiplicar(10, 1), 10)


    #divisao
    def test_divisao_1_0(self):
         self.assertEqual(
             Calculadora.dividir(1, 0), "Valor invalido")
    