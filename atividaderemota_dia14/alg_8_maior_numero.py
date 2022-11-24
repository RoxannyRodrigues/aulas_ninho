numero = []

while len(numero) < 5:
    valores = int(input("Digite um número positivo maior que zero:"))
    if valores != 0:
        numero.append(valores)
    if valores == 0:
        print ("Maior número digitado:", max(numero))
