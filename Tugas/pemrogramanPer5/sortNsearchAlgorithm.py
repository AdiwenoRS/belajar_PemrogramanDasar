print("\nProgram Mengurutkan Data (Bubble Sort)\n")

data = [] #list kosong yang nanti akan di isi oleh userInput
while True:
    try:    #menginput angka
        userInput = int(input("Masukkan angka(masukkan selain angka untuk keluar): "))
        data.append(userInput)
    except: #jika input selain angka
        break
print("Data sebelum diurutkan: ", data) 
for i in data:  #mengurutkan angka
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Data setelah diurutkan: ", data) 

print("\ncari angka yang ingin dicari (Linear Search)")
cari = int(input("Masukkan angka yang ingin dicari: "))

for i in range(len(data)):
    if data[i] == cari:
        print(data)
        print(f"Angka {cari} ditemukan di index {i}")
        break