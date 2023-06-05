"""
Faça um programa que leia 5 números e informe o maior número.
"""


def maior_numero_da_sequencia():
    maior_numero = None
    for c in range(1, 6):
        numero_escolhido = int(input(f'Digite o {c}° numero: '))

        if c == 1:
            maior_numero = numero_escolhido
        elif c > 1:
            if numero_escolhido > maior_numero:
                maior_numero = max(maior_numero, numero_escolhido)

    return maior_numero


if __name__ == '__main__':
    print(maior_numero_da_sequencia())
