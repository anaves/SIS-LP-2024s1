
op = input("Digite (S) p/ soma (M) p/ multiplicar: ")
op = op.strip() # remover espacos do inicio e fim
if op == "S" or op == "s" or op == "M" or op =="m":
    x = float(input("Primeiro valor: "))
    y = float(input("Segundo valor: "))
    if op == "S" or op == "s":
        r = x + y
        print(f"A soma eh {r}")
    else:       #elif op == "M" or op == "m":
        r = x * y
        print(f"A multiplicacao eh {r}")
else:
    print(f"Opcao {op} INCORRETA")