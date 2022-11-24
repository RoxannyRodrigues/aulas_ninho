import numpy as np 

nome = input("Nome do Aluno:")
print (nome)
nota1 = float(input("Digite Primeira Nota:"))
nota2 = float(input("Digite Segunda Nota:"))
nota3 = float(input("Digite Terceira Nota:"))

media = (nota1+nota2+nota3) /3
if media >= 7:
    print(f"{nome} - Aprovado")
elif media <= 5:
    print(f"{nome} - Reprovado")
elif media == np.arange(5.1,6.9):
    print(f"{nome} - Recuperação")


