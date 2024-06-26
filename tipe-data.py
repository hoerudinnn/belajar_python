# tipe data angka tanpa koma (integer)
data_integer = 30
print("data: ", data_integer)
print("- bertipe:", type(data_integer))

# tipe data angka dengan koma (float)
data_float = 1.5
print("data: ", data_float)
print("- bertipe:", type(data_float))

# tipe data kumpulan karakter (string) " "
data_string = "hoerudin"
print("data: ", data_string)
print("- bertipe:", type(data_string))

# tipe data Boolean (True) and Boolean (False)
data_true = True
print("data: ", data_true)
print("- bertipe:", type(data_true))

data_fale = False
print("data: ", data_fale)
print("- bertipe:", type(data_fale))

# tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("data: ", data_complex)
print("- bertipe:", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data: ", data_c_double)
print("- bertipe:", type(data_c_double))