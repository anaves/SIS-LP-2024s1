num_alunos = int(input("Informe quantidade de alunos: "))
notas = []  # criar uma lista vazia
nomes = []  # criar lista vazia pra guardar os nomes
# ler as notas
#soma = 0
for i in range(1, num_alunos+1):
    nome_aluno = input(f"Digite o nome do(a) {i}° aluno(a): ")
    nota_aluno = float(input(f"Nota do(a) {nome_aluno}: "))
    notas.append(nota_aluno)
    nomes.append(nome_aluno)
#    soma += nota_aluno

# calcular a media
media = sum(notas)/len(notas)
print(f"A media da turma foi {media:.1f}")

for indice in range(len(notas)):
    nota = notas[indice]
    nome = nomes[indice]
    if nota > media:
        print(f"{indice} :: {nota} - {nome} parabens!")