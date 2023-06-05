"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""


def inversor_de_10_vetores():
    vetor = list()
    for _ in range(10):
        vetor.append(float(input('Digite o número real: ')))

    return vetor[::-1]


if __name__ == '__main__':
    print(inversor_de_10_vetores())
