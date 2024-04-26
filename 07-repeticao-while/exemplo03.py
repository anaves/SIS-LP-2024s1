import random
sorteado = random.randint(1,500)
# valor sentinela
digitado = -1 # quero um valor inicial distinto

while digitado != sorteado:
    digitado = int(input("Tente adivinhar, digite um numero: "))
    if digitado > sorteado:
        print("o numero deve ser menor")
    elif digitado < sorteado:
        print("o numero deve ser maior")
print("Parabens voce acertou!!!")