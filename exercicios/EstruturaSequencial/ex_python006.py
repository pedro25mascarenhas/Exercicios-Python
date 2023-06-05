"""
Estrutura Sequencial
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""


def area_circulo(raio):
    return 3.14 * raio**2


if __name__ == '__main__':
    r = float(input('Digite o raio do círculo: '))
    print(f'Área do cículo: {area_circulo(r)}')

