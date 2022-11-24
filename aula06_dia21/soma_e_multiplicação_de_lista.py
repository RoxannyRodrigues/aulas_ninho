#Write a Python program to sum all the items in a list
lista = [4,5,8,9,10]
print(lista)
soma = sum(lista)

multiplicação = 1
for numero in lista:
    multiplicação *= numero

print (soma)
print (multiplicação)