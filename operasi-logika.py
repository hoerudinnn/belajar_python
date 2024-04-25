# operator AND
print('===AND===')

a = True
b = True
hasil = a and b
print(a, 'AND', b, '=', hasil)

a = True
b = False
hasil = a and b
print(a, 'AND', b, '=', hasil)

a = False
b = True
hasil = a and b
print(a, 'AND', b, '=', hasil)

a = False
b = False
hasil = a and b
print(a, 'AND', b, '=', hasil)

# operator OR
print('===OR===')

a = True
b = True
hasil = a or b
print(a, 'OR', b, '=', hasil)

a = True
b = False
hasil = a or b
print(a, 'OR', b, '=', hasil)

a = False
b = True
hasil = a or b
print(a, 'OR', b, '=', hasil)

a = False
b = False
hasil = a or b
print(a, 'OR', b, '=', hasil)

# operator NOT
print('===NOT===')

a = True
b = True
hasil = not (a != b)
print(a, 'NOT', b, '=', hasil)  # Output: True NOT True = False

a = True
b = False
hasil = not (a != b)
print(a, 'NOT', b, '=', hasil)

a = False
b = True
hasil = not (a != b)
print(a, 'NOT', b, '=', hasil)

a = False
b = False
hasil = not (a != b)
print(a, 'NOT', b, '=', hasil)