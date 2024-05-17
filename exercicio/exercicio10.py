

fator = 0
sinal = 1
somatorio = 0
tolerancia = 0.001
erro = 100
denominador = 1
pi = 0
while erro > tolerancia:
    numero = sinal*(1/denominador)
    denominador += 2
    somatorio += numero
    # print(f"1/{denominador} = {numero}")
    sinal *= (-1)
    # print(f"somatorio {somatorio}")
    pi_atual = somatorio*4
    erro = abs(pi-pi_atual)
    pi = pi_atual
    print(f"pi = {pi}")
