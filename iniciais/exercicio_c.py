print("="*21)
print("CALCULO DE PESO IDEAL")
print("="*21)

# entrada de dados
altura = float(input("Digita a altura em metros: "))

# processamento
peso_ideal_homem = (72.7*altura) - 58
peso_ideal_mulher = (62.1*altura) - 44.7

# saida
print("-"*25)
print(f"Peso ideal (homem): {peso_ideal_homem:.0f} kg")
print(f"Peso ideal (mulher): {peso_ideal_mulher:.0f} kg")
print("-"*25)

