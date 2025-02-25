# Mensagem inicial
print('Bem-vindo ao aplicativo de vendas de Thiago Agostinho')
quantidadeProdutos = float(input('Qual a quantidade do produto x você gostaria de comprar?'))
valorProduto = float(input('Qual o valor do produto x?'))
# calculo do valor
valorSemDesconto = quantidadeProdutos * valorProduto
# calculo dos descontos
if(valorSemDesconto >= 2500 and valorSemDesconto < 6000):
    valorFinal = valorSemDesconto - (valorSemDesconto * 0.04)
elif(valorSemDesconto >= 6000 and valorSemDesconto < 10000):
    valorFinal = valorSemDesconto - (valorSemDesconto * 0.07)
elif(valorSemDesconto >= 10000):
    valorFinal = valorSemDesconto - (valorSemDesconto * 0.11)
else:
    valorFinal = valorSemDesconto
#Mensagem final da compra
print(f'O valor sem desconto foi de R${valorSemDesconto:.2f} e o valor com o desconto foi de R${valorFinal:.2f}')
