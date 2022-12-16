def soma(numero1, numero2):
    return float(numero1) + float(numero2)

def subtração (numero1, numero2):
    return float(numero1) - float(numero2)

def multiplicação (numero1, numero2):
    return float(numero1) * float(numero2)

def divisão (numero1, numero2):
    if (numero2 == "0"):
        global repetir
        repetir = True
        return "O número 2 não pode ser 0"
        
    else:
        return float(numero1) / float(numero2)

def calculadora (n1,n2,op):
    if(op == "+"):
        print(soma(n1,n2))

    elif (op == "-"):
        print(subtração(n1,n2))

    elif (op == "*"):
        print(multiplicação(n1,n2))

    elif (op == "/"):
        print(divisão(n1,n2))

    else:
        print("Usuário digitou algo errado")
        global repetir
        repetir = True

repetir = True

while(repetir):
    repetir = False
    num1 = input("Escrever o número 1: ")
    num2 = input("Escrever o número 2: ")
   
    operador = input("Escrever o operador (+, -,/,*)")

    if(num1.isnumeric() and num2.isnumeric()):
        calculadora(num1,num2,operador)
    else:
        print("O usuário digitou números inválidos")
        repetir = True
        


    