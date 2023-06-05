"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
"""


def qnt_vendedores_por_faixa_salarial(vetor):
    valor_min = 200
    valor_max = 299
    dicionario_resposta = dict()
    for count, letra in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']):
        if count == 8:
            break
        if count == 7:
            valor_max = float('inf')
        temp = [salario for salario in vetor if valor_min <= salario <= valor_max]

        valor_min += 100
        valor_max += 100

        dicionario_resposta[letra] = len(temp)

    return dicionario_resposta


if __name__ == '__main__':
    salarios_vendedores = [3213, 300, 400, 500, 600, 700, 800, 900, 1000, 2000]
    print(qnt_vendedores_por_faixa_salarial(salarios_vendedores))
