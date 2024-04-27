print("Tugas2")

inputUser = int(input("masukkan data anda:"))

isKurang = inputUser < 3
print(inputUser,"kurang dari 3:", isKurang)

isLebih = inputUser > 10
print(inputUser,"lebih besar dari 10:", isLebih)

isCorrect = isKurang or isLebih
print("angka yang dimasukkan", inputUser, ":", isCorrect)

print("Irisan")

# irisan
inputUser = int(input("masukkan data anda:"))

isLebih = inputUser > 3
print(inputUser, "lebih besar dari 3:", isLebih)

isKurang = inputUser < 10
print(inputUser, "kurang dari 10:", isKurang)

isCorrect = isLebih and isKurang
print("angka yang dimasukkan", inputUser, ':', isCorrect)

# Tugas baru
# ----0++++5----8++++11----
print("===TUGAS BARU===")
inputUser = float(input("masukan nilai anda:"))

nilai1 = inputUser > 0 and inputUser < 5
print(nilai1)

nilai2 = inputUser > 8 and inputUser < 11
print(nilai2)

hasil = nilai1 or nilai2
print(hasil)

print("===IRISAN===")
inputUser = float(input("masukan nilai anda:"))

nilai1 = inputUser < 0 or inputUser > 5
print(nilai1)

nilai2 = inputUser < 8 or inputUser > 11
print(nilai2)

hasil = nilai1 and nilai2
print(hasil)