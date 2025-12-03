# Shift Cipher

def shift_encrypt(text, shift):
    return "".join(chr((ord(ch)-65+shift)%26+65) for ch in text.upper())

print(shift_encrypt("ATTACK", 7))

def shift_decrypt(cipher, shift):
    return shift_encrypt(cipher, -shift)

print(shift_decrypt("HA AHJR", 7))
