print("===KONVERSI SUHU===")

"""
celcius = float(input("Masukan suhu dalam celcius="))
print("suhu dalam celcius adalah=", celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah=", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah=", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah=", kelvin, "kelvin")
"""

# Bagian 1: Fahrenheit ke Kelvin
# Meminta pengguna untuk memasukkan suhu dalam Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
celcius = ((5/9) * fahrenheit) + 32 # Menghitung suhu dalam Celcius
kelvin = celcius + 273 # Menghitung suhu dalam Kelvin
print("Suhu dalam Kelvin =", kelvin, "Kelvin")

# Bagian 2: Kelvin ke Fahrenheit
# Meminta pengguna untuk memasukkan suhu dalam Kelvin
kelvin = float(input("Masukkan suhu dalam Kelvin: "))
celcius = kelvin - 273 # Menghitung suhu dalam Celcius
fahrenheit = ((9/5) * celcius) + 32 # Menghitung suhu dalam Fahrenheit
print("Suhu dalam Fahrenheit =", fahrenheit, "Fahrenheit")
