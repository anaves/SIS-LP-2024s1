valor_1 = int(input("Valor1: "))
valor_2 = int(input("Valor2: "))

maior_que = valor_1 > valor_2
igualdade = valor_1 == valor_2

if maior_que or igualdade:
    print(f"{valor_1} MAIOR OU IGUAL {valor_2}")
else:
    print(f"{valor_2} MAIOR que {valor_1}")
