def comparapalavras(pal1, pal2):
    if (len(pal1) > len(pal2)):
        print(f'A palavra '{pal1}'é maior que a palavra '{pal2}'')
    elif (len(pal1) < len(pal2)):
        print(f"A palavra '{pal2}' é maior que a palavra '{pal1}'")
    elif (len(pal1) == len(pal2)):
        print(f"as palavras '{pal1}' e '{pal2}' tem o mesmo tamanho.")
    