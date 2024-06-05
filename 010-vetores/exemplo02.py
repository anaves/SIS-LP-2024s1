num_alunos = int(input("Informe quantidade de alunos: "))
notas = []  # criar uma lista vazia

# ler as notas
#soma = 0
for i in range(1, num_alunos+1):
    nota_aluno = float(input(f"Nota do {i}°  aluno: "))
    notas.append(nota_aluno)
#    soma += nota_aluno

# calcular a media
media = sum(notas)/len(notas)
print(f"A media da turma foi {media:.1f}")

for indice in range(len(notas)):
    nota = notas[indice]
    if nota > media:
        print(f"{indice} :: {nota} - parabens")