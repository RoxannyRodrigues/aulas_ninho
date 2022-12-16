def gorjetaGarcom (valordaconta):
    print(valordaconta*0.1)
  
  
    
valor= float(input("Valor da conta: "))

if(valor.isnumeric()):
    gorjetaGarcom(float(valor))
else:
    print("Você digitou número inválido")

gorjetaGarcom(valor)
