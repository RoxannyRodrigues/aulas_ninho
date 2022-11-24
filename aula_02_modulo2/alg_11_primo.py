numero =int(input("Digite um númro: "))
mult= 0

for i in range(1, numero + 1):
    if numero % i == 0:
        mult +=1
    
if(mult==2):
    print("É primo")
else:
    print("Não é primo")
