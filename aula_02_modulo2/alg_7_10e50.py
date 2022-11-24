numeros = [None] *10
contador = 0
numerosvalidos = []

for i in range(10):
    numeros[i] = int(input(f"Escreva o número{i+1}: "))


for n in numeros:
    if (n>10 and n<=50):
        numerosvalidos.append(n)
        contador +=1

print(f"Os números digitados entre 10 e 50 foram:{contador} e os números foram {numerosvalidos}")

#como os numerosvalidos não retornar como lista