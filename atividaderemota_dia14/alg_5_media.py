n1 = float(input("Digite a 1ª nota:"))
n2 = float(input("Digite a 2ª nota:"))
n3 = float(input("Digite a 3ª nota:"))
n4 = float(input("Digite a 4ª nota:"))

media = (n1+n2+n3+n4)/4

if media >= 5:
    print ("O aluno foi aprovado com média:", media)
else:
    print ("O aluno não foi aprovado com média:" ,media)


#perguntar se tem outra maneira de aceitar a , e .