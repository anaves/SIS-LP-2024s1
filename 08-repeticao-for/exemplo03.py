for x in range(5):
    print(x)
print("------")
for x in range(10,15):
    print(x)
print("------")
for x in range(90, 100, 2):
    print(x)
print("------")
for x in (1000,1002,5,8):
    print(x)
print("------")
for x in ("Dijkstra","Linus","Ada Lovelace","Turing"):
    print(x)
print("-----------------------")
nomes = ("Dijkstra","Linus","Ada Lovelace","Turing")

for indice, nome in enumerate(nomes):
    print(indice+1, end=" # ")
    print(nome)