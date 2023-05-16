
class Calculadora():

    @staticmethod
    def somar(n, m):
        saida = n + m
        if n + m == saida:
            resultado = n + m
            return resultado


    def subtrair(n, m):
        saida = n - m
        if n - m == saida:
            resultado = n - m
            return resultado
        


    def multiplicar(n, m):
        saida = n * m
        if n * m == saida:
            resultado = n * m
            return resultado

    def dividir(n, m):
        if m == 0:
            return 'Valor invalido'
        saida = n / m
    
        if n / m == saida:
            resultado = n / m
            return resultado
    