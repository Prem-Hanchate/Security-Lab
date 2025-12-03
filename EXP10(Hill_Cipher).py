# Hill Cipher

import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'

    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i])-65], [ord(text[i+1])-65]])
        cipher = np.dot(key, pair) % 26
        result += chr(cipher[0][0]+65) + chr(cipher[1][0]+65)
    return result

key = np.array([[3,3],[2,5]])
print(hill_encrypt("HELLO", key))

def hill_decrypt(cipher, key):
    det = int(np.round(np.linalg.det(key))) % 26
    det_inv = pow(det, -1, 26)
    key_inv = det_inv * np.array([[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]) % 26

    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i])-65], [ord(cipher[i+1])-65]])
        plain = np.dot(key_inv, pair) % 26
        result += chr(int(plain[0][0])+65) + chr(int(plain[1][0])+65)
    return result

print(hill_decrypt(hill_encrypt("HELLO", key), key))
