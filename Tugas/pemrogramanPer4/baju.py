kodeBaju = input("Masukkan kode baju [SP/AD]: ")
ukuran = input("Masukkan ukuran baju [S/M]: ")

if kodeBaju == "SP" or kodeBaju == "sp":
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s":
        harga = 450000
    elif ukuran == "M" or ukuran == 'm':
        harga = 500000
elif kodeBaju == "AD" or kodeBaju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == 'm':
        harga = 700000
else:
    merk = "Anda salah input kode baju"

print(f"\nMerk: {merk}")
print(f"Ukuran: {ukuran.upper()}")
print(f"Harga: Rp {harga}")