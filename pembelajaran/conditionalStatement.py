print("number generator")
start = int(input("set first number: "))
last = int(input("set last number: "))

evenOrOdd = int(input("[1] even or [2] odd or [3] nothing to do: "))

starter = start

if evenOrOdd == 1:
    while starter <= last:
        if starter % 2 == 0:
            print(starter)
        starter += 1
elif evenOrOdd == 2:
    while starter <= last:
        if starter % 2 != 0:
            print(starter)
        starter += 1
elif evenOrOdd == 3:
    while starter <= last:
        print(starter)
        starter += 1
else:
    print("wrong input")