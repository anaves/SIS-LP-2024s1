# Crie um programa que dado o nome completo do funcionario gere o login e o e-mail na empresa libertas.edu.br, o login deve ser composto pelo primeiro nome seguido do ultimo nome, separado por .
# exemplo: 
# --------ENTRADA--------
# nome completo: Linus A. Torvalds
# --------SAIDA--------
# login: linus.torvalds
# email: linus.torvalds@libertas.edu.br
nomes = []
while len(nomes) <= 1:
    nome_completo = input("nome completo: ")
    nome_completo = nome_completo.strip()
    nomes = nome_completo.split(" ")
print(nomes)
print(type(nomes))
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]   # -1 acessa o ultimo elemento
login = primeiro_nome + "." + ultimo_nome
login = login.lower()
print(login)
email = login + "@libertas.edu.br"
print(email)