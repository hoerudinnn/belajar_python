# 1. menyambung string (concatenate)

nama_pertama = "Ucup" # inisialisasi variabel nama_pertama dengan nilai "Ucup"
nama_kedua = "D" # inisialisasi variabel nama_kedua dengan nilai "D"
nama_ketiga = "Fame" # inisialisasi variabel nama_ketiga dengan nilai "Fame"

# menggabungkan nama_pertama, nama_kedua, dan nama_ketiga dengan spasi dan tanda apostrof
nama_lengkap = nama_pertama + " " + nama_kedua + "'" + nama_ketiga
print(nama_lengkap) # mencetak nama_lengkap

# 2. menghitung panjang
panjang = len(nama_lengkap) # menghitung panjang string nama_lengkap
print("panjang dari " + nama_lengkap + " = " + str(panjang)) # mencetak panjang dari nama_lengkap

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "Ucup" # inisialisasi variabel d dengan nilai "Ucup"
status = d in nama_lengkap # mengecek apakah d ada di dalam nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status)) # mencetak hasil pengecekan

D = "D" # inisialisasi variabel D dengan nilai "D"
status = D in nama_lengkap # mengecek apakah D ada di dalam nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status)) # mencetak hasil pengecekan

d = "d" # inisialisasi variabel d dengan nilai "d"
status = d not in nama_lengkap # mengecek apakah d tidak ada di dalam nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status)) # mencetak hasil pengecekan

# mengulang string
print("wk"*10) # mencetak string "wk" sebanyak 10 kali
print(20*"wk") # mencetak string "wk" sebanyak 20 kali

# indexing
print("index ke-0: " + nama_lengkap[0]) # mencetak karakter pada index ke-0
print("index ke-1: " + nama_lengkap[1]) # mencetak karakter pada index ke-1
print("index ke-(-1): " + nama_lengkap[-1]) # mencetak karakter pada index ke-(-1)
print("index ke-(-2): " + nama_lengkap[-2]) # mencetak karakter pada index ke-(-2)
print("index ke-[0:3]: " + nama_lengkap[0:4]) # mencetak karakter dari index ke-0 sampai ke-3
print("index ke-[3:7]: " + nama_lengkap[3:8]) # mencetak karakter dari index ke-3 sampai ke-7
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:11:2]) # mencetak karakter pada index ke-0, 2, 4, 6, 8, dan 10

# nilai paling kecil
print("index paling kecil:" + min(nama_lengkap)) # mencetak karakter dengan nilai ASCII paling kecil
# nilai paling besar
print("index paling besar:" + min(nama_lengkap)) # mencetak karakter dengan nilai ASCII paling besar

ascii_code = ord(" ") # mendapatkan nilai ASCII dari karakter spasi
print("ASCII code untuk spasi adalah " + str(ascii_code)) # mencetak nilai ASCII dari spasi
data = 117 # inisialisasi variabel data dengan nilai 117
print("char untuk ASCII 117 adalah " + chr(data)) # mencetak karakter untuk nilai ASCII 117

# 4. operator dalam bentuk method
data = "otong surotong pararotong" # inisialisasi variabel data dengan nilai string
jumlah = data.count("o") # menghitung jumlah karakter 'o' dalam string data
print("jumlah o pada " + data + " = " + str(jumlah)) # mencetak jumlah karakter 'o' dalam data