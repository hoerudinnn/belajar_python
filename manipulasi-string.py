# 1. menyambung string (concatenate)

nama_pertama = "Ucup"
nama_kedua = "D"
nama_ketiga = "Fame"

nama_lengkap = nama_pertama + " " + nama_kedua + "'" + nama_ketiga
print(nama_lengkap)

# 2. menghitung panjang
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "Ucup"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))