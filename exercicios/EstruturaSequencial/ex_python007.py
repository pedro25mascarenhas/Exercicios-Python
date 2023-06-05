"""
Estrutura Sequencial
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""


def dobro_area_quadrado(numero):
    return numero ** 2 * 2


if __name__ == '__main__':
    lado = float(input('Digite o lado do quadrado: '))
    print(f'Área do quadrado x 2: {dobro_area_quadrado(lado)}')
