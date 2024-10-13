print("Perhitungan gaji pokok karyawan PT. Dingin Damai")
namaKaryawan = input("Nama karyawan: ")
golonganJabatan = int(input("Masukkan Golongan Jabatan [1-3]: "))
pendidikan = input("Masukkan pendidikan SMA/D1/D3/S1: ").upper()
jmlhJamKerja = int(input("Masukkan jam kerja: "))
gajiPokok = 300000

if golonganJabatan == 1:
    tunjanganJabatan = 5 * gajiPokok / 100
elif golonganJabatan == 2:
    tunjanganJabatan = 10 * gajiPokok / 100
elif golonganJabatan == 3:
    tunjanganJabatan = 15 * gajiPokok / 100
else:
    tunjanganJabatan = "Input Golongan jabatan salah"

if pendidikan == "SMA":
    tunjanganPendidikan = 2.5 * gajiPokok / 100
elif pendidikan == "D1":
    tunjanganPendidikan = 5 * gajiPokok / 100
elif pendidikan == "D3":
    tunjanganPendidikan = 20 * gajiPokok / 100
elif pendidikan == "S1":
    tunjanganPendidikan = 30 * gajiPokok / 100
else:
    tunjanganPendidikan = "Input pendidikan salah"

if jmlhJamKerja >= 8:
    honorLembur = (jmlhJamKerja - 8) * 3500

print("\n\n")
print(f"Karyawan yang bernama: {namaKaryawan}")
print("Honor yang diterima,")
print(f"\tTunjangan Jabatan:\t : Rp{int(tunjanganJabatan)}")
print(f"\tTunjangan Pendidikan\t : Rp{int(tunjanganPendidikan)}")
print(f"\tHonor Lembur\t\t : Rp{int(honorLembur)}")
print(f"\nTotal Gaji: Rp{int(gajiPokok + tunjanganJabatan + tunjanganPendidikan + honorLembur)}")