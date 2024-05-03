opcao = 0   # vamos definir um valor inicial
while opcao != 3:
    print("-------------------------------")
    print("1- Somar 2 numeros")
    print("2- Subtrair 2 numeros")
    print("3- Sair")
    opcao = int(input("Digite a opcao: "))

    if opcao == 1 or opcao == 2:
        valor1 = float(input("digite valor: "))
        valor2 = float(input("digite valor: "))
        if opcao == 1:
            resultado = valor1 + valor2
        else:
            resultado = valor1 - valor2
        print(f"o resultado foi {resultado}")
    elif opcao != 3:
        print("opcao invalida")
print("FIM")  
