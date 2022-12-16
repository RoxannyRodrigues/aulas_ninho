# unidades = ("unidade","dezena","centena", "milhar", "dezena de milhar", "centena de milhar", "milhão")

# while(True):

#     numero = input("Escreva um número inteiro de até 7 digitos: ")
#     numeroInvertido = []

#     if (numero.isnumeric()):
#         if (len(numero) <= 7):
#             for i in range(len(numero)):
#                 numeroInvertido.append(numero[(-i-1)])
            
#             for x in range(len(numeroInvertido)):
#                 print(f"{unidades[x]} = {numeroInvertido[x]}")
#             break

#         else:
#             print('Você deve escrever um npumero de até 7 digitos')
#     else:
#         print("Você digitou algum caractere que não é número")


numero = int(input("Insira um número inteiro: "))

resposta = numero

m = 0
c = 0
d = 0
u = 0

while(resposta !=0):
    if(resposta>=1000):
        resposta -=1000
        m += 1
    elif (resposta >=100):
        resposta -= 100
        c +=1
    elif (resposta >= 10):
        resposta -= 10
        d +=1
    elif (resposta >= 1):
        resposta -= 1
        u +=1
    else: break

print(f"Número atual {numero} número de milhares {m} número de centenas {c} número de dezena {d} número de unidade {u}")
