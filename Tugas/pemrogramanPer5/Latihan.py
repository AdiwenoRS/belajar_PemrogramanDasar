ulang = int(input("Ingin memasukkan berapa data? "))
for i in range(ulang):
    print("data ke - " + str(i+1))
    nama = input("Masukkan NIM anda : ")
    uts = int(input("Masukkan Nilai UTS anda : "))
    uas = int(input("Masukkan Nilai UAS anda : "))
    print("NIM anda adalah %s, nilai UTS anda %i, nilai UTS anda %i" % (nama, uts, uas))
    print("-"*50)