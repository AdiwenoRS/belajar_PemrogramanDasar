from datetime import date

today = date.today()
tahunLahir = int(input("Masukkan tahun lahir anda: "))
bulanLahir = int(input("Masukkan bulan lahir anda: "))
tanggalLahir = int(input("Masukkan tanggal lahir anda: "))
date = [int(today.strftime("%Y")), int(today.strftime("%m")), int(today.strftime("%d"))]
yearCalc = (date[0] - tahunLahir)

if (bulanLahir >= date[1] and tanggalLahir >= date[2]):
    yearCalc -= 1

print("Umur anda adalah", yearCalc, "Tahun")
