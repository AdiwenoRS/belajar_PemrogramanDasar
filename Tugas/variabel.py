var1 = "Hello world"
var2 = "I love python"

print(var1)
print(var1[0])
print(var2[2:6])
print(var2[2:])
print(var2[:6])
print(len(var1))

split = var1.split(" ")
print(split)
print(split[0])

print("Artha\'s code")

print(r"this \n is printable")
print("ini adalah \x41\x52\x54\x48\x41")

defaultOrder = "{}, {} ,dan {}".format("dua", "tiga", "empat")
print(defaultOrder)
positionalOrder = "{2}, {0} ,dan {1}".format("dua", "tiga", "empat")
print(positionalOrder)


print("format biner: {0:b}".format(10)) 
print("format eksponensial: {0:e}".format(10.34))

x = 12.3456789 
print("nilai x %3.5f" %x)

print(round(1.1+2.2))