import random

numero_pc = [1, 2, 3 ,4 ,5 ,6 ,7 ,8, 9]
pc = random.choice(numero_pc)
usuario = 0

while usuario != pc:
    usuario=int(input("Adivinhe o numero PC vai escolher: "))
    print("Tente novamente")

print("Palpite bem-sucedido")
