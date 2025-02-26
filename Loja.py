#Acumulador
valor = 0

#Mensagem de entrada e tabela de preços
print(' ' * 10, 'Bem-vindos a loja do Thiago Agostinho\n')
print(' ' * 10, 'Tamanho', ' ' * 5, 'Cupuaçu', ' ' * 5, 'Açaí\n',
' ' * 10, 'P', '   ', ' ' * 4, 'R$ 9,00', ' ' * 4, 'R$ 11,00\n',
' ' * 10, 'M', '   ', ' ' * 4, 'R$ 14,00', ' ' * 3, 'R$ 16,00\n',
' ' * 10, 'G', '   ', ' ' * 4, 'R$ 18,00', ' ' * 3, 'R$ 20,00\n')
#Inicia o loop de pedidos
while True:
    # Verifica o sabor e reinicia o loop se estiver errado
    sabor = input('Qual sabor você gostaria de comprar?(CP/AC)').strip().upper()
    if sabor != 'CP' and sabor != 'AC':  
        print('Sabor inválido. Tente novamente.') 
        continue  
    # Verifica o tamanho e reinicia o loop se estiver errado
    tamanho = input(f'Qual o tamanho do {sabor}? (P/M/G) ').strip().upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':  
        print('Tamanho inválido. Tente novamente.') 
        continue  
    # Adiciona o valor correspondente às escolhas do usuário
    if sabor == 'CP' and tamanho == 'P':
        valor += 9
    elif sabor == 'CP' and tamanho == 'M':
        valor += 14 
    elif sabor == 'CP' and tamanho == 'G':
        valor += 18
    elif sabor == 'AC' and tamanho == 'P':
        valor += 11
    elif sabor == 'AC' and tamanho == 'M':
        valor += 16
    elif sabor == 'AC' and tamanho == 'G':
        valor += 20
    # Pergunta se o usuário gostaria de continuar
    continuar = input('Deseja pedir mais alguma coisa?').strip().upper()
    if continuar != 'SIM':
        break
    
# Exibe a mensagem final com o valor total
print(f'seu pedido ficou no total de R$ {valor:.2f}')