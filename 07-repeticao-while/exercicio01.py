"""
num = 7

soma = 0X | 3X | 11X | 11X | 12X | 17X | 24

3
8
0
1
5
7
"""
import random
digitado = 0
while digitado < 1 or digitado > 10:
    digitado = int(input("digite um numero entre 1 e 10: "))
sorteado = -1
soma = 0
while sorteado != digitado:
    sorteado = random.randint(1,10)
    soma = soma + sorteado
    print(f"sorteado = {sorteado} soma = {soma}")