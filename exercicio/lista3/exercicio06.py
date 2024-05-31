n = int(input("Quantos numeros perfeitos vc precisa?: "))
qtd = 0
numero = 1
while qtd < n:
    # busca_perfeito
    metade = numero // 2   # divisao inteira
    soma = 0
    for divisores in range(1,metade+1):
        if numero % divisores == 0:
            # print(divisores)
            soma = soma + divisores
    if soma == numero:
        qtd += 1
        print(f"numero: {numero} eh perfeito")
    numero = numero + 1