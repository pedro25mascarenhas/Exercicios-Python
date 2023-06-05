"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""


def analisar_string(string_1, string_2):
    tamanho_1 = len(string_1)
    tamanho_2 = len(string_2)

    print('String 1: {}'.format(string_1))
    print('String 2: {}'.format(string_2))
    print('')
    print(f'Tamanho de "{string_1}": {tamanho_1}')
    print(f'Tamanho de "{string_2}": {tamanho_2}')

    is_tamanho_igual = 'As duas strings são de tamanhos iguais' if tamanho_1 == tamanho_2 \
        else 'As duas strings são de tamanhos diferentes'
    is_conteudo_igual = 'As duas strings possuem conteudos iguais' if string_1.split() == string_2.strip() \
        else 'As duas strings possuem conteúdo diferente'

    print('')
    print(is_tamanho_igual)
    print(is_conteudo_igual)


if __name__ == '__main__':
    string_1 = 'Brasil hexa 2006'
    string_2 = 'Brasil! Hexa 2006!'
    analisar_string(string_1, string_2)
