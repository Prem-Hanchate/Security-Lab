# Caesar Cipher (Monoalphabetic Substitution)

def caesar_encrypt(text, shift):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result

print("Encrypted: " + caesar_encrypt("HELLO", 3))

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

print("Decrypted: " + caesar_decrypt("KHOOR", 3))
