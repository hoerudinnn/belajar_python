# Meminta pengguna untuk memasukkan nama dan menyimpannya dalam variabel 'user'
user = input("Masukkan nama anda: ")  
print("Nama: ", user) # Menampilkan nama yang dimasukkan oleh pengguna

# Meminta pengguna untuk memasukkan pesan dan mengonversinya menjadi string
message = input("Masukkan pesan anda: ")  
print("Pesan anda:", message)

# Meminta pengguna untuk memasukkan data (0 atau 1), mengonversi menjadi integer, kemudian menjadi boolean
biner = bool(int(input("Masukkan data anda: ")))  
print("Data anda:", biner, "- Tipe data:", type(biner)) # Menampilkan data yang dimasukkan oleh pengguna beserta tipe datanya
