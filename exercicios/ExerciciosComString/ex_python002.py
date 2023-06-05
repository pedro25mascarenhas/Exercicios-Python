"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""


if __name__ == '__main__':
    nome = input('Digite um nome qualquer: ')
    nome_reverso_maiusculo = nome[::-1].upper().split()
    nome_reverso_maiusculo_2 = ''.join(reversed(nome)).upper().split()
    print(nome_reverso_maiusculo)
    print(nome_reverso_maiusculo_2)
