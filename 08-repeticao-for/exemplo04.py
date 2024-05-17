# imprimir os numeros pares entre 2 numeros
inicio = int(input("digite o valor inicial: "))
final = int(input("digite o valor final: "))

for v in range(min(inicio,final),max(inicio,final)):
    if v % 2 == 0:
        print(f"{v} eh par")
    else: 
        print(f"{v} eh impar")