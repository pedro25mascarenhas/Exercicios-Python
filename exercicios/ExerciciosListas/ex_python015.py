"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""


def analise_de_vetor():
    vetor = list()
    print('#### OBS: Para sair digite o valor -1')
    while True:
        numero = float(input('Digite o número real: '))
        if numero == -1:
            break
        vetor.append(numero)
    tamanho_vetor = len(vetor)
    soma = sum(vetor)
    media = round(soma/len(vetor), 2)
    valores_acima_da_media = [elemento for elemento in vetor if elemento > media]
    valores_abaixo_de_7 = [elemento for elemento in vetor if elemento < 7]

    resolucao = {
        'A': tamanho_vetor,
        'B': vetor,
        'C': c(vetor),
        'D': soma,
        'E': media,
        'F': valores_acima_da_media,
        'G': valores_abaixo_de_7,
    }
    print('')

    print(''.join(f'{key}: {value}\n' for key, value in resolucao.items()))


def c(vetor):
    vetor_str = ''
    vetor.reverse()
    for i in vetor:
        vetor_str += f'[{i}]\n'
    return vetor_str


if __name__ == '__main__':
    analise_de_vetor()
    print('\nObrigado por ter utilizado o nosso script :D')
