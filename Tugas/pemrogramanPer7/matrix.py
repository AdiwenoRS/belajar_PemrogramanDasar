matrix1 = [    
    [9, 0],
    [3, 6]
]

matrix2 = [    
    [6, 0],
    [7, 2]
]
print("Hasil penjumlahan matrix")
for x in range(len(matrix1)):
    for y in range(len(matrix1)):
        print(matrix1[x][y] + matrix2[x][y], end = " ")
    print()

print("\n Hasil pengurangan matrix")
for x in range(len(matrix1)):
    for y in range(len(matrix1)):
        print(matrix1[x][y] - matrix2[x][y], end = " ")
    print()

print("\nHasil perkalian matrix")
matrix3 = []

for x in range(len(matrix1)):
    row = []
    for y in range(len(matrix1)):
        total = 0
        for z in range(len(matrix1)):
            total = total + (matrix1[x][z] * matrix2[z][y])
        row.append(total)
    matrix3.append(row)

print("matrix3")
for x in range(len(matrix3)):
    for y in range(len(matrix3)):
        print(matrix3[x][y], end = " ")
    print()