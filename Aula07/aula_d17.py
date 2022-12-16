palavra = input("Insira uma palavra:")

while (True):

    letra = input("Insira apenas um caractere: ")
    if (len(letra) == 1):
        break
    else:
        print("Você inseriu mais que um caractere, insira novamente!")

print(f"O caractere '{letra}' a palavra '{palavra}' apareceu {checagem} vezes")
 