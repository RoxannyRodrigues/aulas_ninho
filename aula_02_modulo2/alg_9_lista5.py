valores = []
while len(valores) < 5:
    numeros = int(input("Digite 5 números:"))
    valores.append(numeros)

for numero in valores:
    numero = min(valores)
    print("Menor número digitado foi:" ,min(valores))
    break