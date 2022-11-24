cardapio = {
    '100': ['Cachorro quente', 1.10],
    '101': ['Bauru Simples', 1.30],
    '102': ['Bauru com ovo', 1.50],
    '103': ['Hamburguer', 1.10],
    '104': ['Chessburguer', 1.10],
    '105': ['Refrigerante', 1.00],
}

pedido = {}
while True:
    codigo = input('Informe o codigo')
    if (codigo =='0'):
        break
    if codigo in cardapio:
        quant = int(input("Informe a quantidade: "))
        if quant > 0:
            Valor = cardapio.get(codigo)
            pedido.update({codigo:(Valor, quant)})

valordopedido = 0

for linha in pedido.itens():
    valordopedido += linha [1][0][1] * [1][1] 

print("\nSeu Pedido: ")

for linha in pedido.itens():
     print(str(linha[1][1]) + ' x ' + 'R$ ' + str(round(linha[1][0][1], 2)) + ' --- ' + str(linha[1][0][0]))

print('\nTOTAL DO PEDIDO: R$ ' + str(round(valordopedido, 2)))
