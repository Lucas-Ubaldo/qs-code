class Empregado():
    def __init__(self, primeiro_nome, sobrenome, cargo, salario):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        self.taxa_reajuste = 1.05

    def calcular_reajuste(self):
        novo_salario = self.salario * self.taxa_reajuste 
        return novo_salario

    def gerar_nome_completo(self):
        nome_completo = self.primeiro_nome + self.sobrenome
        return nome_completo
    
    def validar_cargo(self):
        cargos_empresa = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']
        if self.cargo in cargos_empresa:
            return 'OK'
        else:
            return "Cargo invalido"