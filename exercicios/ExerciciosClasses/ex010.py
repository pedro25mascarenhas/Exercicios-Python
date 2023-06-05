"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaDeCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipoCombustivel = tipo_combustivel
        self.valorLitro = valor_litro
        self.quantidadeCombustivel = quantidade_combustivel

    def litros_por_dinheiro(self, dinheiro: float):
        quantidade_litros = round(dinheiro / self.valorLitro, 2)
        self.quantidadeCombustivel -= quantidade_litros
        return quantidade_litros

    def valor_por_litros(self, litros: float):
        return litros * self.valorLitro

    def alterar_valor(self, novo_valor: float):
        self.valorLitro = novo_valor

    def alterar_combustivel(self, novo_combustivel: str):
        self.tipoCombustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade: float):
        self.quantidadeCombustivel = nova_quantidade


bomba = BombaDeCombustivel('Gasolina', 5.75, 200)
bomba.alterar_valor(10)
bomba.alterar_combustivel('Álcool')
bomba.alterar_quantidade_combustivel(2302)
print(bomba.tipoCombustivel, bomba.valorLitro, bomba.quantidadeCombustivel)

print(bomba.litros_por_dinheiro(12), bomba.valor_por_litros(12.5))
