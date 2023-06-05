"""
Estrutura Sequencial
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def fahrenheit_para_celsius(f):
    return 5 * (f-32)/9


if __name__ == '__main__':
    fahrenheit = float(input('Digite os graus em Fahrenheit: '))
    print(f'Convertido para Celsius: {fahrenheit_para_celsius(fahrenheit):.2f}')
