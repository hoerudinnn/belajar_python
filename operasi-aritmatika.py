a = 10
b = 3

# pertambahan +
hasil = a + b
print(a, '+', b, '=', hasil)

# pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# sisa bagi %
hasil = a % b
print(a, '%', b, '=', hasil)

# pangkat **
hasil = a ** b
print(a, '**', b, '=', hasil)

# pembagian bulat //
hasil = a // b
print(a, '//', b, '=', hasil)


x = 3
y = 5
z = 7

hasil = x + y * z // x - z ** y / x % z
print(x,'+',y,'*',z,'//',x,'-',z,'**',y,'/',x,'%',z, '=', hasil)