a = 5 # operator assignment (=)
a += 2 # (+)
print("nilai a 5, setelah += menjadi:", a)

a = 5
a -= 2 # (-)
print("nilai a 5, setelah -= menjadi:", a)

a = 5
a *= 2 # (*)
print("nilai a 5, setelah *= menjadi:", a)

a = 5
a /= 2 # (/)
print("nilai a 5, setelah /= menjadi:", a)

print("===================================")

b = 7
b //= 2 # (//)
print("nilai b 7, setelah //= menjadi:", b)

b = 7
b %= 2 # (//)
print("nilai b 7, setelah %= menjadi:", b)

b = 7
b **= 2 # (**)
print("nilai b 7, setelah **= menjadi:", b)

print("===================================")

c = True
c &= True
print("hasil:", c)
c = False
c &= True
print("hasil:", c)

c = True
c |= False
print("hasil:", c)
c = False
c |= True
print("hasil:", c)

c = False
print(c)
c ^= True
print("hasil:", c)
c = False
c ^= True
print("hasil:", c)

d = 0b00010
print(d)
d >>= 2
print("hasil:", d)

d = 0b00010
print(d)
d <<= 2
print("hasil:", d)