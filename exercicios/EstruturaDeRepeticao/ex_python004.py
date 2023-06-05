"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""


def anos_para_ultrapassagem_pais_a():
    populacao_pais_a = 80_000
    taxa_anual_de_crescimento_pais_a = 1.03
    populacao_pais_b = 200_000
    taxa_anual_de_crescimento_pais_b = 1.015

    contador = 0
    while populacao_pais_a < populacao_pais_b:
        populacao_pais_a *= taxa_anual_de_crescimento_pais_a
        populacao_pais_b *= taxa_anual_de_crescimento_pais_b

        contador += 1
        print(contador, int(populacao_pais_a), int(populacao_pais_b))
    return contador


if __name__ == '__main__':
    print(anos_para_ultrapassagem_pais_a())
