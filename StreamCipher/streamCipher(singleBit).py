import sys

MSGS = ["Hello my name is Bob", "Goodbye from Stephen"]

def strxor(a, b):     # xor two strings of different lengths
    return "".join([chr(ord(a[0]) ^ ord(b[0]))])
    

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

key = "weiognwoingweoignwoiggoiwnegoiwngwoingwigngoiwngwoingwoignwiognwiongw"
ciphertexts = [encrypt(key, msg) for msg in MSGS]


