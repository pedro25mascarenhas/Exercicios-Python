"""
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminno, M - Masculino, Sexo inválido.
"""


def masculino_ou_feminino(escolha):
    if escolha[0] == 'F':
        print('Feminino')
    elif escolha[0] == 'M':
        print('Masculino')
    else:
        print('Sexo inválido')


if __name__ == '__main__':
    masculino_ou_feminino(input('Selecione o sexo (M/F): ').upper())
