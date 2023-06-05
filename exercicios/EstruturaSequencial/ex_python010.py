"""
Estrutura Sequencial
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def celsius_para_fahrenheit(c):
    return c * 9/5 + 32


if __name__ == '__main__':
    celsius = float(input('Digite os graus em Celsius: '))
    print(f'Convertido para Celsius: {celsius_para_fahrenheit(celsius):.2f}')
