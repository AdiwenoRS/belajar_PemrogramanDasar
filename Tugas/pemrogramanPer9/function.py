def sapa(nama):
    print("hi "+ nama + ". Apa kabar?")
    
sapa(nama = "Shifa")

def print_info(nama, usia = 17):
    print("nama ", nama)
    print("usia ", usia)
    
print_info(nama = "Galih", usia = 20)
print_info(nama = "Galih")

def sum(a, b):
    total = a + b
    return total

sum(2, 5)


def print_info(arg1, *vartuple):
    print("output:")
    print(arg1)
    print(vartuple)
    
print_info(2, 4, 5, 6)