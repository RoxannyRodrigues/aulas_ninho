def checarletra(l,p):
    if(p.count(l)):
        print(f"A letra '{l}' existe na palavra '{p}' ")
    else:
        print(f"A letra '{l}' naõ existe na palavra '{p}' ")

checarletra("a", "teste")
checarletra("c", "cachorro")