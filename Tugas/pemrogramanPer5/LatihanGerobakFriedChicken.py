print(f"GEROBAK FRIED CHICKEN\n{50*'-'}")
print("Kode\tJenis Potong\tHarga\n", 50*"-")
print("D\tDada\t\tRp2500")
print("P\tPaha\t\tRp2000")
print("S\tSayap\t\tRp1500")
print(50*"-")

# Data for the table
jenisPotong = []
banyakPotong = []
hargaSatuan = []
jumlahHarga = []
jumlahBayar = 0 

#Input for create data to table
banyakPesanan = int(input("Banyak pesanan: "))
for i in range(banyakPesanan):
    print(f"\nJenis ke-{i+1}")
    # Input 
    inputKodePotong = input("Kode potong [D/P/S]: ").upper()
    inputBanyakPotong = int(input("Banyak potong: "))
    # Add to database
    banyakPotong.append(inputBanyakPotong)
    # Add to database based on inputKodePotong input
    if inputKodePotong == "D":
        jumlahHarga.append(2500 * inputBanyakPotong)
        hargaSatuan.append(2500)
        jenisPotong.append("Dada")
    elif inputKodePotong == "P":
        jumlahHarga.append(2000 * inputBanyakPotong)
        hargaSatuan.append(2000)
        jenisPotong.append("Paha")
    elif inputKodePotong == "S":
        jumlahHarga.append(1500 * inputBanyakPotong)
        hargaSatuan.append(1500)
        jenisPotong.append("Sayap")

#Show table
print(f"\nGEROBAK FRIED CHICKEN\n{70*'-'}")
print(f"No.\tJenis Potong\tHarga Satuan\tBanyak Beli\tJumlah Harga\n{70*"-"}")
#Show all data from table
#print(kodePotong, hargaSatuan, banyakPotong, jumlahHarga)  #remove hastag to print the original data form
for i in range(banyakPesanan):
   print(f"{i+1}\t{jenisPotong[i]}\t\t{hargaSatuan[i]}\t\t{banyakPotong[i]}\t\tRp{jumlahHarga[i]}")
   jumlahBayar += jumlahHarga[i]
    

print(70*"-")
print(f"\t\t\t\t\t\t\tJumlah bayar Rp{jumlahBayar}")
pajak = jumlahBayar*10/100
print(f"\t\t\t\t\t\t\tPajak 10% Rp{pajak}")
print(f"\t\t\t\t\t\t\tTotal bayar Rp{jumlahBayar+pajak}")
