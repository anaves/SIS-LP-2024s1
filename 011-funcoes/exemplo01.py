
def le_inteiro(coisa):
    numero = int(input(coisa))
    # print(f"numero digitado = {numero}")
    return numero

idade = le_inteiro("digite idade: ")
quantidade = le_inteiro("digite quantidade de pessoas: ")

print(f"idade: {idade}")
print(f"quantidade: {quantidade}")
