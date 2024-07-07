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

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(20*"wk")

# indexing
print("index ke-0: " + nama_lengkap[0])
print("index ke-1: " + nama_lengkap[1])
print("index ke-(-1): " + nama_lengkap[-1])
print("index ke-(-2): " + nama_lengkap[-2])
print("index ke-[0:3]: " + nama_lengkap[0:4])
print("index ke-[3:7]: " + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:11:2])

# nilai paling kecil
print("index paling kecil:" + min(nama_lengkap))
# nilai paling besar
print("index paling besar:" + min(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))