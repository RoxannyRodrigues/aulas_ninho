s = input("Digite o seu sexo (F) ou (M):")
s = s.upper()
a = (input("Digite a sua altura"))
af = float(a.replace(',','.'))

pf = (62.1 * af ) - 44.7 

pm = (72.7 * af) - 58

if s == "F":
    print("Seu peso ideal é:", ("%.3f" % pf))
elif s == "M":
    print("Seu peso ideral é:", ("%.3f" % pm))
else:
    print("Digite um sexo válido")

#explicar locale 
#limitar casa decimais >>>> ("%.limitef" % variavellimitar)