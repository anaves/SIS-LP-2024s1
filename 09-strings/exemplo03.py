texto =  "Lorem ipsum"
print(len(texto))
# print(texto[3])
# print(texto[0])
# print(texto[10])
#print(texto[11]) # erro
vogais = ["A","E","I","O","U","a","e","i","o","u"]
qtd = 0
for indice in range(len(texto)):
    print(indice, end=" # ")
    letra =  texto[indice]
    print(letra)
    if letra in vogais:
        print("......  vogal")
        qtd += 1
print(f"Temos {qtd} vogais no texto: {texto}")