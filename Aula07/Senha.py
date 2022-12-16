#Insira uma senha de no mínimo 4 digitos e no máximo 8 devendo conter apenas números#

repetir = True
def verificar_senha(senha):
    global repetir
    if len(senha) >=4 and len(senha) <=8:
        if senha.isnumeric():
            repetir = False
        print ("Senha valida")
    else:
        print ("Você digitou senha invalida")

senha = input("Digite sua senha: ")
verificar_senha(senha)


