matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("=== Matriz 3x3 ===")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ") 
    print()
print("\n=== Elementos por Coordenada ===")
elem1 = matriz[0][1]
elem2 = matriz[2][2]
print(f"Elemento [0][1] = {elem1}") 
print(f"Elemento [2][2] = {elem2}")  
soma_diagonal = 0

for l in range(3):
    for c in range(3):
        if l == c:  
            soma_diagonal += matriz[l][c]

print("\n=== Resultado ===")
print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")
