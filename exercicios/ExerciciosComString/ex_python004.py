"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
"""


def escada_invertida(str):
    for i in range(1, len(str)+1):
        print(str[:i])


if __name__ == '__main__':
    palavra = 'FULANO'
    escada_invertida(palavra)
