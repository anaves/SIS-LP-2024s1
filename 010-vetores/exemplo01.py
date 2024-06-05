notas = [3.5,8.7,5,6.9,5.4,8]
print(notas)
print(notas[2])
notas[3] = 10
print(notas)
# adicionar uma nova nota na lista
notas.append(9)
print(notas)
qtd = len(notas)
for indice in range(qtd):
    valor = notas[indice]
    print(f"{indice}:: conteudo: {valor}")
    if valor >= 6:
        print(">>>>>>>>> PARABENS <<<<<<<<<<<")