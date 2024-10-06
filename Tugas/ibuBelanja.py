'''
Ibu pergi ke pasar membeli telur sebanyak 5 kilogram untuk membuat kue, harga 1 kilo
gram telor adalah 26000 per kilogram. untuk pergi ke pasar ibu harus naik angkot pulang
pergi dengan tarif 3500 sekali naik angkot. Pertanyaan: Berapakah sisa uang jika ibu membawa 
uang sebesar 200000'''
#input: berat telur(brt), harga telur(hrg), transport(ongkos), uang ibu(uang)
#output: sisa uang(sisa)
print("\n\nIbu pergi ke pasar membeli telur sebanyak 5 kilogram untuk membuat kue, harga 1 kilo\ngram telor adalah 26000 per kilogram. untuk pergi ke pasar ibu harus naik angkot pulang\npergi dengan tarif 3500 sekali naik angkot. Pertanyaan: Berapakah sisa uang jika ibu membawa\nuang sebesar 200000\n\n")

brt = int(input("Berat telur (kg): "))
hrg = int(input("Harga telur (Rp): "))
ongkos = int(input("Ongkos angkot(Rp): "))
uang = int(input("Uang Ibu(Rp): "))

sisa = uang - (brt * hrg) - (ongkos*2)
print(f"\nSisa uang: Rp{sisa}")

