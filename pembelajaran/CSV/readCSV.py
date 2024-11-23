import csv

with open('/home/artha/Documents/Codingan_ARTHA/belajar_PemrogramanDasar/pembelajaran/CSV/people.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)