# NIM/Nama  : 16922096/ Nabila Syahidah
# Tanggal   : 07/10/2022
# Deskripsi : program untuk menentukan faktor prima suatu bilangan

x = int(input('masukkan n: '))    
primeNumber = []
  
for i in range(2,x+1):
    if(x % i == 0 ):
        prime = True
        for j in range(2,(i//2+1)):
            if i % j == 0:
                prime = False
        if prime == True:
            primeNumber.append(i)
print(primeNumber)          
