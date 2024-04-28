# or (|)
print("==========OR==========")
a = 9
b = 5
c = a | b

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', b, 'binary:', format(b, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))

# and (&)
print("==========AND==========")
a = 9
b = 5
c = a & b

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', b, 'binary:', format(b, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))

# xor (^)
print("==========XOR==========")
a = 9
b = 5
c = a ^ b

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', b, 'binary:', format(b, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))

# not (~)
print("==========NOT==========")
c = ~a

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))
d = 0b0000001001
e = 0b1111111111
print('nilai', e^d, 'binary:', format(e^d, '08b'))

# shifting
# shift right (>>)
print("==========SHIFT RIGHT==========")
c = a >> 2

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))

# shift right (<<)
print("==========SHIFT LEFT==========")
c = a << 2

print('nilai', a, 'binary:', format(a, '08b'))
print('nilai', c, 'binary:', format(c, '08b'))