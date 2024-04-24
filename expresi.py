x = 10
y = 2
result = x + y

print(result)

angka = [1,2,3,4,5]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

# replikasi list
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)

''' 
Ekspresi Menurut Arity dari Operator
Jenis	Contoh
Biner (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

Uner (x += 1), (x-=1), (not x).
'''

a = True
a = not a
print (a)

b = 6
b -= 1
print (b)

c = 6
c += 1
print (c)

d = 10
print (-d)

'''
Ekspresi Menurut Tipe Data yang Dihasilkan
Jenis	Contoh
Ekspresi aritmetika: 
<numerik> <operator> <numerik> = <numerik>
2 + 2 = 4, 2 - 2 = 0

Ekspresi relasional: 
<numerik> <operator> <numerik> = <boolean>
3 < 10 = True, 1 > 10 = False

Ekspresi logika: 
<boolean> <operator> <boolean> = <boolean>
True or False = True
'''

print (2+2)
print (3<10)
print (True or False)

# operator aritmatika
xx = 11
yy = 5

print (xx + yy) #penjumlahan
print (xx - yy) #pengurangan
print (xx * yy) #perkalian
print (xx // yy) #pembagian bulat
print (xx / yy) #pembagian rill
print (xx % yy) #modulo
print (xx ** yy) # pangkat

# operator relasional
angka1 = 5
angka2 = 10

print (angka1 == angka2)
print (angka1 != angka2)
print (angka1 > angka2)
print (angka1 < angka2)
print (angka1 >= angka2)
print (angka1 <= angka2)

dico = 750000
if dico > 500000:
    diskon = 0.1 * dico
    total_harga = dico - diskon
else:
    total_harga = dico

print (total_harga)

xxx = 1960 
yyy = 901 
print(xxx % yyy) 