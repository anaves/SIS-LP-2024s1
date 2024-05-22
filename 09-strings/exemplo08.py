nome_completo = input("digite nome completo: ")
partes = nome_completo.split()
# print(partes)
sobrenome = partes[-1] # obtemos o ultimo termo
tamanho = len(partes)

citacao = sobrenome.upper() + ", "
for indice in range(tamanho-1):
    parte = partes[indice]
    inicial = parte[0]
    # print(parte)
    citacao += inicial + ". "
print(citacao)

