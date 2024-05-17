texto =  "Lorem ipsum"
print(len(texto))

vogais = ["A","E","I","O","U","a","e","i","o","u"]
qtd = 0
for letra in texto:
    print(letra)
    if letra in vogais:
        print("......  vogal")
        qtd += 1
print(f"Temos {qtd} vogais no texto: {texto}")