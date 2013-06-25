c1 = "6c73d5240a948c86981bc2808548".decode('hex')
c2 = "0d07a14569fface7ec3ba6f5f623".decode('hex')

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


print(strxor(c1, c2).encode('hex'))
