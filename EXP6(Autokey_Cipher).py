# Autokey Cipher

def autokey_encrypt(plain, key):
    key_stream = key + plain
    cipher = ""
    for p, k in zip(plain.upper(), key_stream.upper()):
        cipher += chr(((ord(p)-65) + (ord(k)-65)) % 26 + 65)
    return cipher

print(autokey_encrypt("HELLO", "K"))


def autokey_decrypt(cipher, key):
    plain = key
    result = ""
    for i, c in enumerate(cipher):
        p = (ord(c) - 65) - (ord(plain[i]) - 65)
        p = (p + 26) % 26
        plain += chr(p + 65)
        result += chr(p + 65)
    return result

print(autokey_decrypt(autokey_encrypt("HELLO","K"), "K"))
