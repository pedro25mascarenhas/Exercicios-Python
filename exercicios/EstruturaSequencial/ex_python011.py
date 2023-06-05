"""
Estrutura Sequencial
9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


if __name__ == '__main__':
    numero_inteiro_um = int(input('Digite o primeiro numero inteiro: '))
    numero_inteiro_dois = int(input('Digite o segundo numero inteiro: '))
    numero_real = float(input('Digite um numero real: '))

    print(numero_inteiro_um * numero_inteiro_dois/2)
    print(numero_inteiro_um * 3 + numero_real)
    print(f'{numero_real**3:.2f}')
