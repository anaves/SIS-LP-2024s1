import random

X = int(input("Digite a quantidade: "))
soma=0
for _ in range(X):
    num = random.randint(1,10)
    soma+=num
    print(num)
print("=============")
print(soma)