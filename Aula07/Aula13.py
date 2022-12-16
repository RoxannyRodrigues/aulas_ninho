
palavra1 = input("Digite a primeira palavra")
palavra2 = input("Digite a segunda palavra")

def comparação(pal1,pal2):
    
    if len(pal1) > len(pal2):
        return True

    else:
        return False

print(comparação(palavra1,palavra2))