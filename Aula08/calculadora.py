repetir = True

while repetir:
    
    repetir = False

    num1 = ("Digite o primeiro número: ")

    if (num1.isnumeric()):
        
        num1 = float(num1)
        num2 = ("Digite o segundo número: ")

        if (num2.isnumeric()):
            num2 = float(num2)

            operador = input("Digite a operação([+ ou soma],[- ou subtração],[/ ou divisão],[* ou multiplicação]): ")
            
            if (operador == "+" or operador.lower() == "soma"):
                print("A soma é:", num1+num2)

            elif (operador == "-" or operador.lower() == "subtração"):
                print("A subtração é:", num1-num2)

            elif (operador == "*" or operador.lower() == "multiplicação"):
                print("A multiplicação é:", num1*num2)

            elif (operador == "/" or operador.lower() == "divisão"):
                if (num2 == 0):
                    repetir = True
                    print("Você tentou dividir por 0, operação inválida!")
            else:
                    repetir = True
                    print("Você digitou operador inválido!") 
