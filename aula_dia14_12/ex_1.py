class Triangulo:
    def __init__ (self, ladoA, ladoB, LadoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = LadoC
        self.maiorLado = ""

    def calcularPerimetro(self):

        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def getMaiorLado(self):

        if(self.ladoA >= self.ladoB and self.ladoA >= self.ladoC):
            self.maiorLado = self.ladoA
        elif(self.ladoB >= self.ladoA and self.ladoB >= self.ladoC):
            self.maiorLado = self.ladoB
        elif(self.ladoC >= self.ladoA and self.ladoC >= self.ladoB):
            self.maiorLado = self.ladoC
        else:
            self.maiorLado = "Alguns lados são iguais"

triangulo1 = Triangulo(8,8,7)

print(triangulo1.calcularPerimetro())

triangulo1.getMaiorLado()
print(triangulo1.maiorLado)