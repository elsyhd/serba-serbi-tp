# NIM/Nama  : 16922096/ Nabila Syahidah
# Tanggal   : 07/10/2022
# Deskripsi : program untuk  mencari jumlah setiap bilangan yang lebih besar dari bilangan tepat sebelumnya. Tuan Kil akan terus memberikan angka hingga angka tidak lebih besar dari angka sebelumnya sebanyak 3 kali berturut-turut.
# notes: kak kalo ini di-run ga jalan yaudahlahya maafin aku, aku bingung sekali :((
x = 1
sum = 0
num1 = int(input('angka ke-'+ str(x) + ':'))


tidakLebihDari = 0
while tidakLebihDari < 3:
    x = x + 1
    num2 = int(input('angka ke-'+ str(x) + ':'))
    if num1 >= num2:
        tidakLebihDari = tidakLebihDari + 1
    if num1 < num2:
        sum = sum + num2
        tidakLebihDari = 0
    num1 = num2
print(sum)