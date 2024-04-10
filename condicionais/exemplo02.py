numero = int(input("Digite: "))
resto = numero%2    # % calcula o resto da divisao
if resto == 0:
    print(f"{numero} eh par")
    if numero < 0:
        print("ele eh NEGATIVO")
    else:
        print("ele eh POSITIVO")
else:
    print(f"{numero} eh impar")
    if numero < 0:
        print("ele eh NEGATIVO")
    else:
        print("ele eh POSITIVO")