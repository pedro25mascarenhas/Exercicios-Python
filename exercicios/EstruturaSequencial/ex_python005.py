"""
Estrutura Sequencial
5. Faça um Programa que converta metros para centímetros.
"""


def metros_para_centrimetros(metros):
    return metros*100


if __name__ == '__main__':
    centimetros = metros_para_centrimetros(float(input('Digite a metragem que vai ser convertida: ')))
    print(f'Convertido para centímetros: {centimetros}')
