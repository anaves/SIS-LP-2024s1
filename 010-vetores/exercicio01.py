A = []
B = []
C = []

# PREENCHER VALORES
for i in range(3):
    c_a = float(input(f"Coordenada {i+1} do A: "))
    c_b = float(input(f"Coordenada {i+1} do B: "))
    A.append(c_a)
    B.append(c_b)

# mostrar o vetores
print(f"A = {A}")
print(f"B = {B}")

# CALCULAR RESULTADO
for i in range(len(A)):
    C.append(A[i]+B[i])

print("-RESULTADO-")
print(f"C = {C}")