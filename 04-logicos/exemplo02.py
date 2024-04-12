valor_1 = int(input("digite valor1: "))
valor_2 = int(input("digite valor2: "))

igualdade =  valor_1==valor_2
print(f"A afirmacao que {valor_1} eh igual {valor_2} eh {igualdade}")
print(type(igualdade))

if igualdade:
    print("SAO IGUAIS")
else:   # if not igualdade:
    print("SAO DIFERENTES")

print("FIM DO PROGRAMA")