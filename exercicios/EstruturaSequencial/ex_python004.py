"""
Estrutura Sequencial
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def media():
    numero = 0
    for contador in range(1, 5):
        numero += float(input(f'Digite a nota {contador}: '))
    return numero/4


if __name__ == '__main__':
    print(f'A média das suas notas é: {media()}')
