# Vigenère Cipher

def vigenere_encrypt(text, key):
    cipher = ""
    key = key.upper()
    j = 0
    for ch in text.upper():
        c = (ord(ch)-65 + ord(key[j]) - 65) % 26
        cipher += chr(c + 65)
        j = (j + 1) % len(key)
    return cipher

print(vigenere_encrypt("HELLO", "KEY"))


def vigenere_decrypt(cipher, key):
    key = key.upper()
    result = ""
    j = 0
    for ch in cipher:
        p = (ord(ch)-65 - (ord(key[j])-65)) % 26
        result += chr(p + 65)
        j = (j + 1) % len(key)
    return result

print(vigenere_decrypt(vigenere_encrypt("HELLO","KEY"), "KEY"))
