"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_valor_lado(self, novo_lado):
        self.lado = novo_lado

    def valor_lado(self):
        return self.lado

    def area(self):
        return self.lado ** 2


quadrado_teste = Quadrado(2)
quadrado_teste.mudar_valor_lado(4)
print(quadrado_teste.valor_lado(), quadrado_teste.area())
