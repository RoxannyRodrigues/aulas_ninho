"""Enunciado = Fazer um programa onde seja inserido nomes de alunos e a quantidade de equipes.
Esses alunos tem que ser organizados na equipe com quantidades iguais.
Obs: O divisão das equipes fica a seu critério"""

equipe = []


while len(equipe) <5 :
    aluno = input("Nome do Aluno")
    equipe.append(aluno)
    break 

print(equipe)
