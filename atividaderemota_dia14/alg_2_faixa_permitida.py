num = input("Digite um valor")
numf = float(num.replace(',','.')) #usuario pode usar . ou ,

if (numf >= 1) and (numf <= 9):
    print("O valor está na faixa permitida")

else:
    print("O valor não está na faixa permitida")
