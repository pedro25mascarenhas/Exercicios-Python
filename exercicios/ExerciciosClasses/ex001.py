"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


bola_um = Bola()
bola_um.troca_cor('Amarelo')

print(id(bola_um), bola_um.mostra_cor())
