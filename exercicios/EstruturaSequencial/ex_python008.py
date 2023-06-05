"""
Estrutura Sequencial
8. Faça um Programa que pergunte quanto ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""


def calcular_salario_mensal(horas_trabalhadas_no_mes, salario_por_hora):
    return horas_trabalhadas_no_mes * salario_por_hora


if __name__ == '__main__':
    horas_trabalhadas_no_mes = int(input('Digite as horas que trabalhou no mês: '))
    salario_por_hora = float(input('Digite quanto ganha por hora: '))
    print(f'Salário que deve receber no mês: {calcular_salario_mensal(horas_trabalhadas_no_mes, salario_por_hora)}')

