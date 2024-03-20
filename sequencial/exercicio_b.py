
print("-----------------------------------------------")
print("-----------Digite notas entre 0 e 10-----------")
print("-----------------------------------------------")
# entrada de dados
prova1 = float(input("digite a nota da Prova 1: "))
prova2 = float(input("digite a nota da Prova 2: "))
trabalho = float(input("digite a nota do Trabalho: "))
participacao = float(input("digite a nota de Participacao: "))

# processamento
provas = 3*prova1 + 3*prova2
media =  (provas + 3*trabalho + participacao) / 10

# saida
print(f"Sua media foi de: {media}")