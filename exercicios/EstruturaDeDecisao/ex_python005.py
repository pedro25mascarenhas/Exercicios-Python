"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def situacao_aluno(parcial1, parcial2):
    media = (parcial1 + parcial2) / 2
    if media >= 7:
        print('Aprovado')
    elif media < 7:
        print('Reprovado')
    elif media == 10:
        print('Aprovado com Distinção')


if __name__ == '__main__':
    situacao_aluno(int(input('Digite a nota 1: ')), int(input('Digite a nota 2: ')))
