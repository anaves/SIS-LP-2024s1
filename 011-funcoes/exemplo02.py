
def calcula_media(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    media = soma / len(lista)
    print(f"a media foi de {media}")

print("NAME")
print(__name__)
if __name__ == "__main__":
    calcula_media([1,2,3,4,5,6])
    calcula_media([10,20,30])
    calcula_media([100,200,300,400])
    calcula_media([1000,2000,3000])