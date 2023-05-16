import unittest
from empregado import Empregado

class EmpregadoTeste(unittest.TestCase):
    
    

    def test_calcular_reajuste_50000(self):
        e1 = Empregado('cassio', 'ramos', 'presidente', 50000)
        saida = e1.calcular_reajuste()
        esperado = 52500
        self.assertEqual(saida, esperado)
    
    def test_gerar_nome_completo(self):
        e1 = Empregado('cassio', 'ramos', 'presidente', 50000)
        saida = e1.gerar_nome_completo()
        esperado = 'cassioramos'
        self.assertEqual(saida, esperado)


