"""
Estrutura Sequencial
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

"""
from math import ceil
from math import floor


def calculadora_latas_e_despesa(area):
    area *= 1.1
    litros = area / 6
    latas = litros / 18
    valor_latas = ceil(latas) * 80
    galoes = litros / 3.6
    valor_galoes = ceil(galoes) * 25

    maximo_de_latas_possivel = floor(latas)
    litros_excedentes = litros % 18
    galoes_para_completar = ceil(litros_excedentes / 3.6)
    valor_latas_e_galoes = maximo_de_latas_possivel * 80 + galoes_para_completar * 25

    return {
        'Area': round(area, 2),
        'Litros': round(litros, 2),
        'Latas': ceil(latas),
        'Valor Latas': valor_latas,
        'Galoes': ceil(galoes),
        'Valor Galoes': valor_galoes,
        'Valor Latas e Galoes': valor_latas_e_galoes

    }


if __name__ == '__main__':
    area = float(input('Digite a área (m²): '))
    print(calculadora_latas_e_despesa(area))
