"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""


def escada_invertida(str):
    for i in range(len(str)):
        print(str[:len(str) - i])


if __name__ == '__main__':
    palavra = 'FULANO'
    escada_invertida(palavra)
