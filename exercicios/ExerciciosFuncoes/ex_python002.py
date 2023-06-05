"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""


def piramide_de_numeros(n: int):
    for i in range(1, n + 1):
        for j in range(1, i+1):
            print(j, end='    ')
        print('')


if __name__ == '__main__':
    entrada = 12
    piramide_de_numeros(entrada)
