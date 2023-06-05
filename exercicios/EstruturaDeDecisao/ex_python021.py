"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


def saque(valor):
    notas_disponiveis = [100, 50, 10, 5, 1]
    dicionario_de_cedulas = dict()
    if 10 > valor > 600:
        print('O caixa não pode fornecer o valor solicitado')
    else:
        for cedula in notas_disponiveis:
            qnt_cedulas, valor = divmod(valor, cedula)
            dicionario_de_cedulas[f'Cédulas de {cedula}'] = qnt_cedulas
        return dicionario_de_cedulas


if __name__ == '__main__':
    print(saque(int(input('Informe o valor do saque: '))))
