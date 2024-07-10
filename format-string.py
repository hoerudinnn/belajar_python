# contoh generic
# string
nama = "hoer"
format_str = f"Hello, {nama}"
print(format_str)

boolean = True
format_str = f"Boolean adalah = {boolean}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"Desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"Desimal = {angka:020.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +100.12345
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# format persen
persentase = 0.045
format_str = f"persentase = {persentase:.2%}"
print(format_str)

# melakukan operasi aritmatika
harga = 1000
jumlah = 5
format_str = f"harga total = rp. {harga*jumlah:,}"

print(format_str)

# menampilkan angka lain (binary, octal, dan hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)