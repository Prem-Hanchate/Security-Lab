# Additive Cipher

def additive_encrypt(text, key):
    return "".join(chr((ord(ch)-65 + key) % 26 + 65) for ch in text.upper())

print(additive_encrypt("HELLO", 5))

def additive_decrypt(cipher, key):
    return additive_encrypt(cipher, -key)

print(additive_decrypt("MJQQT", 5))
