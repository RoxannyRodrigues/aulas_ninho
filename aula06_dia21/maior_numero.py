#Write a Python program to get the largest number from a list.
numero = []
while len(numero) < 5:
    valores = int(input("Digite valores da lista:"))
    numero.append(valores)

print ("Maior número digitado:", max(numero))
print ("Menor número digitado:", min(numero))


#para nao aparecer a frase Digite valores...