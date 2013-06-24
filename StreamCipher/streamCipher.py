import sys

MSGS = ["Hello my name is Bob", "Goodbye from Stephen"]

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

key = "weiognwoingweoignwoiggoiwnegoiwngwoingwigngoiwngwoingwoignwiognwiongw"
ciphertexts = [encrypt(key, msg) for msg in MSGS]


