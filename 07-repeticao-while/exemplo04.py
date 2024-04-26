# Programa que imprime a quantidade de
# números pares de 100 até 200, incluindo-os

qtd = 0
n = 100
while n <= 200:
    resto = n%2
    if resto == 0:
        qtd += 1
    n += 1
print(f"Tem {qtd} pares entre [100,200]")