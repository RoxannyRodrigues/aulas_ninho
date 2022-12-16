def potencia(a,b):
    resultado = 1

    while (b>0):
        resultado = resultado*a
        return resultado

base = (input("Digite um número"))
expoente = (input("Digite o expoente"))

print(potencia(int(base), int(expoente)))
