"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""


def media_e_soma():
    media = soma = 0
    for c in range(1, 6):
        numero_escolhido = int(input(f'Digite o {c}° numero: '))

        soma += numero_escolhido
        media = round(soma/5, 2)

    return soma, media


if __name__ == '__main__':
    print(media_e_soma())
