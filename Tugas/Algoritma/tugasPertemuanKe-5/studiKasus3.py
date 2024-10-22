piramidRow = int(input("right triangle row: "))

for i in range(1, piramidRow + 1):
    for k in range(2 * i - 1):
        print("*", end="")
    print()
        