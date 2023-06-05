"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""


def bytes_in_megabytes(bytes):
    return round(bytes / 1024 ** 2, 2)


def percentual_de_uso(espaco_utilizado, espaco_total_utilizado):
    return round(espaco_utilizado * 100 / espaco_total_utilizado, 2)


if __name__ == '__main__':
    endereco = 'arquivos/usuarios.txt'

    with open(endereco, 'r') as arquivo:
        data_list = list()
        data_dict = {'usuario': '', 'espaco_utilizado': '', 'percentual': ''}
        contador = espaco_total_utilizado = 0

        for linha in arquivo:
            linha = linha.split()
            usuario = linha[0]
            espaco_utilizado_em_megabytes = bytes_in_megabytes(int(linha[1]))
            espaco_total_utilizado += espaco_utilizado_em_megabytes

            data_dict['usuario'] = usuario
            data_dict['espaco_utilizado'] = espaco_utilizado_em_megabytes
            data_list.append(data_dict.copy())

        for data in data_list:
            data['percentual'] = f"{percentual_de_uso(data['espaco_utilizado'], espaco_total_utilizado)}%"
            data['espaco_utilizado'] = f"{data['espaco_utilizado']} MB"

        print(data_list)

        cabecalho = """ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""

    with open('arquivos/relatorio_gerado.txt', 'w') as arquivo:
        arquivo.writelines(cabecalho)
        for indice, dados in enumerate(data_list):
            arquivo.writelines(f"{indice:<4} {dados['usuario']:14} {dados['espaco_utilizado']:>16} {dados['percentual']:>12}\n")

        arquivo.writelines(f'\nEspaço total ocupado: {espaco_total_utilizado} MB\n')
        arquivo.writelines(f'Espaço médio ocupado: {round(espaco_total_utilizado/len(data_list), 2)} MB')


