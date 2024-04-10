
op = input("Digite (S) p/ soma (M) p/ multiplicar: ")
op = op.strip() # remover espacos do inicio e fim
op = op.lower() # transformei valor em minusculo
if op == "s" or op =="m":
    x = float(input("Primeiro valor: "))
    y = float(input("Segundo valor: "))
    if op == "s":
        r = x + y
        print(f"A soma eh {r}")
    else:      
        r = x * y
        print(f"A multiplicacao eh {r}")
else:
    print(f"Opcao {op} INCORRETA")