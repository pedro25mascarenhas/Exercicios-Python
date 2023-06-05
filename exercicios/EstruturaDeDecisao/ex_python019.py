"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


def decompor_numeros_menores_que_mil(numero):
    if numero > 999:
        return 'Número inválido'

    else:
        centenas_str = dezenas_str = unidades_str = frase = ''

        centenas_int, numero = divmod(numero, 100)

        if centenas_int == 1:
            centenas_str = '1 centena'
        elif centenas_int > 1:
            centenas_str = f'{centenas_int} centenas'

        dezenas_int, numero = divmod(numero, 10)

        if dezenas_int == 1:
            dezenas_str = '1 dezena'
        elif dezenas_int > 1:
            dezenas_str = f'{dezenas_int} dezenas'

        unidades_int = numero

        if unidades_int == 1:
            unidades_str = '1 unidade'
        elif unidades_int > 1:
            unidades_str = f'{unidades_int} unidades'

        lista_frase = [elemento for elemento in [centenas_str, dezenas_str, unidades_str] if elemento != '']

        if len(lista_frase) == 3:
            frase = lista_frase[0] + ', ' + lista_frase[1] + ' e ' + lista_frase[2]
        elif len(lista_frase) == 2:
            frase = lista_frase[0] + ' e ' + lista_frase[1]
        else:
            frase = centenas_str + dezenas_str + unidades_str

        return frase


if __name__ == '__main__':
    print(decompor_numeros_menores_que_mil(321))
