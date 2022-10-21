jmlLampu = int(input('masukkan banyak lampu: '))
frekuensiTekan = int(input('masukkan berapa kali Tuan Kil menekan tombol:'))
i = 1
tombol = []
j = 1
lampu = []

while i <= frekuensiTekan:
    tombolTekan = int(input('Tombol yang ditekan ke' + str(i) + ':'))
    i += 1
    tombol.append(tombolTekan)

while j <= jmlLampu:
    a = 0
    lampu.append(a)
    j += 1

