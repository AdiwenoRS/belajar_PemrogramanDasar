print("\nRental Mobil Jaya\n")

mobil = ["Toyota", "Honda", "Ford", "BMW", "Mercedes-Benz"]
ketersediaanMobil = ["Tersedia", "Tersedia", "Tersedia", "Tersedia", "Tersedia"]

def listMobil():
    print("-"*50)
    print("No.|\t  Mobil\t\t|\tstatus") 
    print("-"*50)
    for i in range(len(mobil)):
        print(f"{i+1}. |", end=(""))    
        if len(mobil[i]) < 4: # if statement untuk menyesuaikan posisi garis tabel jika nama mobil terlalu panjang atau pendek
            print(f"{mobil[i]}\t\t\t|\t{ketersediaanMobil[i]}")
        elif 12 > len(mobil[i]) > 3:
            print(f"{mobil[i]}\t\t|\t{ketersediaanMobil[i]}") 
        elif len(mobil[i]) > 12:
            print(f"{mobil[i]}\t|\t{ketersediaanMobil[i]}")

while True:
    listMobil() #panggil fungsi listMobil
    print("\nApa yang anda ingin lakukan?")
    inputUser = int(input("1. pinjam mobil\n2. kembalikan mobil\n3. Tambah mobil\n4. hapus mobil\n5. keluar\ninput: "))

    if inputUser == 1: #pinjam mobil
        print("\nMasukkan nomor mobil yang ingin dipinjam")
        pinjam = int(input("input: "))
        for i in range(len(mobil)):
            if ketersediaanMobil[pinjam - 1] == "Dipinjam":
                print("+Mobil sedang dipinjam+\n")
                break
            elif pinjam == i+1: #jika nomor mobil yang dipinjam ada
                ketersediaanMobil.insert(i, "Dipinjam") #status mobil menjadi di pinjam
        if pinjam > (len(mobil)+1): #jika nomor mobil yang dipinjam tidak ada
            print("\nTidak ada mobil yang dipinjam\n")
                
    elif inputUser == 2: #kembalikan
        print("Masukkan nomor mobil yang ingin dikembalikan")
        kembali = int(input("input: "))
        for i in range(len(mobil)):
            if pinjam == i+1: #jika nomor mobil yang dikembalikan ada
                ketersediaanMobil[i] = "Tersedia" #status mobil menjadi tersedia
        if pinjam > (len(mobil)+1): #jika nomor mobil yang dipinjam tidak ada
            print("\nTidak ada mobil yang dipinjam\n")
            
    elif inputUser == 3: #tambah
        print("Masukkan mobil yang ingin ditambahkan")
        tambah = input("input: ")
        mobil.append(tambah) #menambahkan mobil
        
    elif inputUser == 4: #hapus
        print("Masukkan nomor mobil yang ingin dihapus")
        hapus = int(input("input: "))
        for i in range(len(mobil)):
            if hapus == i+1:
                del mobil[i] 
                del ketersediaanMobil[i]
                
    elif inputUser == 5: #keluar
        break
print("Sudah keluar, terimakasih:)")