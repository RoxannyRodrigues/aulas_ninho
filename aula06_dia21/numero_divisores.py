divisiveis = []
multiplos = []
for i in range(1500,1550):
    if i %7 == 0:
       divisiveis.append(i)
    elif i %5 == 0:
        multiplos.append(i)
   
  

print("Os números divisível de 7 são:" ,divisiveis)
print("Os números multiplos de 5 são:" ,multiplos)
