# Operator komparasi digunakan dalam Python untuk membandingkan dua nilai dan menghasilkan nilai kebenaran (True atau False) berdasarkan hasil perbandingan tersebut. Berikut adalah beberapa operator komparasi yang umum digunakan beserta contoh codingannya:

# 1. **Pembanding Sama (==)**:
a = 5 
b = 5
hasil = (a == b)
print(hasil)  # Output: True

# 2. **Tidak Sama (!=)**:
a = 5
b = 7
hasil = (a != b)
print(hasil)  # Output: True

# 3. **Lebih Besar (>)**:
a = 7
b = 5
hasil = (a > b)
print(hasil)  # Output: True

# 4. **Lebih Kecil (<)**:
a = 5
b = 7
hasil = (a < b)
print(hasil)  # Output: True

# 5. **Lebih Besar atau Sama (>=)**:
a = 7
b = 5
hasil = (a >= b)
print(hasil)  # Output: True

# 6. **Lebih Kecil atau Sama (<=)**:
a = 5
b = 7
hasil = (a <= b)
print(hasil)  # Output: True


a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Menggunakan operator 'is' untuk memeriksa apakah dua variabel merujuk ke objek yang sama
hasil1 = (a is b)
hasil2 = (a is c)

print(hasil1)  # Output: False, karena a dan b menunjuk ke objek yang berbeda meskipun isinya sama
print(hasil2)  # Output: True, karena a dan c menunjuk ke objek yang sama
