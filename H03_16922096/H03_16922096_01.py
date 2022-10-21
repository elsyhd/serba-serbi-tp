i = 0
j = 0
banyakBarang = int(input('masukkan banyak barang:'))

hargaAwal = [int(input('masukkan harga awal barang ke-' + str(i+1)+':')) for i in range (banyakBarang)]
i+= 1

besarDiskon = [int(input('masukkan besar diskon (dalam persen) barang ke-' + str(j+1)+':')) for j in range (banyakBarang)]

hargaAkhir = []
for val1, val2 in zip(hargaAwal, besarDiskon):
    hargaAkhir.append(val1*val2/100)

max = hargaAkhir[0]
for k in hargaAkhir:
    if k > max:
        max = k
print('barang', i , 'memiliki diskon paling besar yaitu', round(max))