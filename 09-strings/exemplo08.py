nome_completo = input("digite nome completo: ")
partes = nome_completo.split()
# print(partes)
sobrenome = partes[-1] # obtemos o ultimo termo
tamanho = len(partes)
eliminar = ["da", "das", "do", "dos", "de"]
citacao = sobrenome.upper() + ", "

for indice in range(tamanho-1):
    parte = partes[indice]
    if parte not in eliminar:
        inicial = parte[0]
        citacao += inicial + ". "

print(citacao)

