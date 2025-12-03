# Multiplicative Cipher

def mul_encrypt(text, key):
    return "".join(chr(((ord(ch)-65) * key) % 26 + 65) for ch in text.upper())

print(mul_encrypt("HELLO", 7))



# Decryption - Need modular inverse of key.

def mod_inverse(a, m=26):
    for i in range(m):
        if (a*i) % m == 1:
            return i
    return None

def mul_decrypt(cipher, key):
    inv = mod_inverse(key)
    return "".join(chr((inv * (ord(ch)-65)) % 26 + 65) for ch in cipher)

print(mul_decrypt(mul_encrypt("HELLO", 7), 7))
