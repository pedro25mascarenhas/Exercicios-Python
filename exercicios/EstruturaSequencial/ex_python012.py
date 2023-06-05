"""
Estrutura Sequencial
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def calculadora_peso_ideal(h):
    return 72.7*h - 58


if __name__ == '__main__':
    altura = float(input('Digite a altura: '))
    print(f'{calculadora_peso_ideal(altura):.2f}')
