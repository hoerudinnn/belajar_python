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
