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

# format leading zero
angka = 2005.54321
format_str = f"Desimal = {angka:020.3f}"
print(format_str)

