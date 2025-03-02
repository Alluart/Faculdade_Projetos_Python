print("Bem-vindo a copiadora do Thiago Agostinho") 
#Função para escolher o serviço
def escolha_servico():
    while True:
        serv = input("Digite o serviço desejado:\nDigitalização (DIG)\nColorida (ICO) \nPreto e Branco (IPB) \nFotocópia (FOT)").strip().upper()
        if serv == "DIG":
            return 1.10
        elif serv == "ICO":
            return 1
        elif serv == "IPB": 
            return 0.40
        elif serv == "FOT": 
            return 0.20

        else:
            print("Serviço inválido. Tente novamente.")
#Função para escolher o numero de paginas
def num_pagina():
    while True:
        try:
            num = int(input("Qual o numero de paginas:"))
            if num < 20:
                return num # Sem desconto
            elif 20 <= num < 200:
                return num * 0.85 # 15% de desconto
            elif 200 <= num < 2000:
                return num * 0.80 # 20% de desconto
            elif 2000 <= num < 20000:
                return num * 0.75 # 25% de desconto
            else:
                print("O numero desejado excede o limite permitido.")
        except ValueError:
            print("Entre com a quantidade de paginas novamente")
#Função para escolher o serviço extra
def servico_extra():
    try:
        while True:
            ext = int(input('Qual servço extra voce gostaria:\nencadernação simples (1) \nencadernação de capa dura (2)\não querer mais nada (0)'))
            if ext == 1:
                return 15
            elif ext == 2:
                return 40
            elif ext == 0:
                return 0
    except ValueError:  # Caso o usuário insira um valor não numérico
        print('Serviço extra invalido. Escolha novamente.')

# Chamadas das funções para coletar as informações
servico = escolha_servico()
num_paginas = num_pagina()
extra = servico_extra()

# Cálculo do valor total
total = (servico * num_paginas) + extra
print(f"O valor total do serviço é: R$ {total:.2f}")
