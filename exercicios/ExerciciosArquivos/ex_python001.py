"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""


def validar(ip: str) -> bool:
    numeros = ip.split('.')
    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    if len(numeros) != 4:
        return False

    return True


if __name__ == '__main__':
    endereco = 'arquivos/enderecos_ip.txt'

    with open(endereco, 'r') as arquivo:
        lista_validos = lista_invalidos = list()
        for linha in arquivo:
            ip = linha.strip()
            if validar(ip):
                lista_validos.append(ip)
            else:
                lista_invalidos.append(ip)

    with open('arquivos/ips_saida.txt', 'w') as arquivo:

        arquivo.writelines('IPs validos: \n')
        for ip in lista_validos:
            arquivo.writelines(f'{ip}\n')

        arquivo.writelines('\n')

        arquivo.writelines('IPs invalidos: \n')
        for ip in lista_invalidos:
            arquivo.writelines(f'{ip}\n')
