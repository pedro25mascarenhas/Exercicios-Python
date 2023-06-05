"""
Estrutura Sequencial
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def calculadora_peso_ideal(h):
    return {'Homens': round(72.7*h - 58, 2), 'Mulheres': 62.1*h - 44.7}


if __name__ == '__main__':
    altura = float(input('Digite a altura: '))
    print(f'Pesos ideais: {calculadora_peso_ideal(altura)}')
