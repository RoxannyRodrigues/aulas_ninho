valores = []
while len(valores) < 3:
    numeros = int(input("Digite três valores diferente"))
    valores.append(numeros)
numeros_decrescente = sorted(valores, reverse=True)
print(numeros_decrescente)