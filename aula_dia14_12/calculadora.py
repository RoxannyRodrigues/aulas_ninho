class Calculadora:
    def __init__(self):
        self.numero1 = ""
        self.numero2 = "" 
        self.operador = ""
    
    def soma(self):
        soma = self.numero1 + self.numero2
        self.numero1 = soma
        return soma 

    def subtracao(self):
        subtracao = self.numero1 - self.numero2
        self.numero1 = subtracao
        return subtracao

    def multiplicacao(self):
        multiplicacao = self.numero1 * self.numero2
        self.numero1 = multiplicacao
        return multiplicacao  

    def divisao(self):
        divisao = self.numero1 / self.numero2
        self.numero1 = divisao
        return divisao 



calculadora = Calculadora()

while True:

    if (calculadora.numero1 ==""):
        calculadora.numero1 = int(input("Insira o número 1: "))

    calculadora.numero2 = int(input("Insira o número 2: "))
    calculadora.operador = input("Insira o operador: ")

    if(calculadora.operador == "+"):
        print(calculadora.soma())
    

