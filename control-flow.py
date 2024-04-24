stock = "tempe"

if stock == "daging ayam":
    print ('Ibu membeli daging ayam dan memasaknya')
else:
    print ('Ibu membeli tempe dan memasaknya')


# ternary operators
lulus = True
print("selamat") if lulus else print("perbaiki") #bernilai true -> kondisi -> bernilai false

# ternary tuples
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus] #bernilai false, true -> kondisi
print(kelulusan)

#perulangan
#menggunakan for
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

for j in range(10):
    print(j)

for a in range(1,10,2):
    print(a)

#menggunakan while
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

#break 
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

#continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# else setelah for
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

# else setelah while
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

#pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

#list comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

for aa in range(1, 3):    
    for bb in range(1, 3):    
    print(aa, bb)