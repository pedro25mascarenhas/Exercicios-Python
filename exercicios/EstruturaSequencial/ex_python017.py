"""
Estrutura Sequencial
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""
from math import ceil


def calculadora_latas_e_despesa(area):
    return {
        'Area': area,
        'Litros': (area / 3),
        'Latas': ceil(area / (3 * 18)),
        'Valor': ceil(area / (3 * 18) * 80)
    }


if __name__ == '__main__':
    area = float(input('Digite a área (m²): '))
    print(calculadora_latas_e_despesa(area))
