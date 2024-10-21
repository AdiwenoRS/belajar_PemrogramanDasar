startN = int(input("enter a start of number range: "))
endN = int(input("enter an end of number range: "))
b = 0
for i in range(startN, endN):
    print(i, end=" + ")
    b += i
print(f"{endN} = {b + endN}")