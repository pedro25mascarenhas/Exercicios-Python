"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, tempo_em_anos):
        if self.idade <= 21:
            tempo_para_crescer = (21 - self.idade) if self.idade + tempo_em_anos > 21 else tempo_em_anos
            self.altura += tempo_para_crescer * 0.05
        self.idade += tempo_em_anos

    def engordar(self, peso_em_quilos):
        self.peso += peso_em_quilos

    def emagrecer(self, peso_em_quilos):
        self.peso -= peso_em_quilos

    def crescer(self, altura_em_centimetros):
        self.altura += altura_em_centimetros/100


pedro = Pessoa('Pedro', 18, 73, 1.8)
pedro.envelhecer(10)
pedro.crescer(3.1)
pedro.engordar(10)
pedro.emagrecer(5)

print(pedro.altura, pedro.idade, pedro.peso)
