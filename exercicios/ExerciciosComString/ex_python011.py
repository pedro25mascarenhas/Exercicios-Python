"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

from random import randint

def jogo_da_forca(lista_de_palavras):
    palavra_sorteada = lista_de_palavras[randint(0, len(lista_de_palavras)-1)].upper()
    print(palavra_sorteada)
    conjunto_letras_palavra_sorteada = set(palavra_sorteada)
    conjunto_letras_digitadas = set()
    
    tentativas = 0
    while tentativas < 6:
        letra = input('Digite a letra: ').upper()
        conjunto_letras_digitadas.add(letra)

        if letra in conjunto_letras_palavra_sorteada:
            for letra in palavra_sorteada:
                if letra in conjunto_letras_digitadas:
                    print(f'{letra} ', end='')
                else:
                    print(f'_ ', end='')
            print('')

            if conjunto_letras_palavra_sorteada.issubset(conjunto_letras_digitadas):
                print('')
                print('VOCÊ GANHOU !')

        else:
            tentativas += 1

        if tentativas == 6:
            print('VOCÊ PERDEU.... TENTE NOVAMENTE')


if __name__ == '__main__':
    lista_de_palavras = ['LOREM', 'IPSOM']
    jogo_da_forca(lista_de_palavras)

