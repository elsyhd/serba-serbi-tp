# NIM/Nama  : 16922096/ Nabila Syahidah
# Tanggal   : 04/10/2022
# Deskripsi : program menentukan suatu bilangan merupakan bilangan sempurna atau bukan

n = int(input('masukkan sebuah bilangan: '))
factors =[]

for x in range(1,n):
    if n % x == 0:
        factors.append(x)
        
if (sum(factors)) == n :
    print('Bilangan tersebut adalah bilangan sempurna.')
else:
    print('Bilangan tersebut bukan bilangan sempurna.')

    

