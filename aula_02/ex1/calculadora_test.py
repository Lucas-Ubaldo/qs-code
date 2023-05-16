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

    def test_subtracao_59_9(self):
         self.assertEqual(
             Calculadora.subtrair(59, 9), 50)


    #multiplicação
    def test_multiplicacao_10_1(self):
         self.assertEqual(
             Calculadora.multiplicar(10, 1), 10)

    def test_multiplicacao_89_0(self):
         self.assertEqual(
             Calculadora.multiplicar(89, 0), 0)

    def test_multiplicacao_2_8(self):
         self.assertEqual(
             Calculadora.multiplicar(2, 8), 16)


    #divisao
    def test_divisao_1_0(self):
         self.assertEqual(
             Calculadora.dividir(1, 0), "Valor invalido")
    
    def test_divisao_10_1(self):
         self.assertEqual(
             Calculadora.dividir(10, 1), 10)

    def test_divisao_100_3(self):
         self.assertEqual(
             Calculadora.dividir(100, 2), 50)
    