# RSA Encryption and Decryption

# Find modular inverse of e mod phi
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Encrypt: C = (M^e) % n
def rsa_encrypt(message, e, n):
    return pow(message, e, n)

# Decrypt: M = (C^d) % n
def rsa_decrypt(cipher, d, n):
    return pow(cipher, d, n)

# RSA Key Setup
p, q = 11, 13              # Two prime numbers
n = p * q                   # n = 143
phi = (p - 1) * (q - 1)    # phi = 120
e = 7                       # Public exponent
d = mod_inverse(e, phi)     # Private exponent (d = 103)

# Encryption and Decryption
original = 9
encrypted = rsa_encrypt(original, e, n)
decrypted = rsa_decrypt(encrypted, d, n)

print(f"Original Message: {original}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Public Key: ({e}, {n})")
print(f"Private Key: ({d}, {n})")
