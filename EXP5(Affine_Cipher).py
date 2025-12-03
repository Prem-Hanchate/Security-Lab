# Affine Cipher

# Function to find modular inverse of a under modulo 26
def mod_inverse(a):
    # Find a number that when multiplied with 'a' and mod 26 gives 1
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

# Encrypt text using Affine Cipher
def affine_encrypt(text, a, b):
    cipher = ""
    for ch in text.upper():
        if ch.isalpha():  # Only encrypt letters
            p = ord(ch) - 65  # Convert letter to number (A=0, B=1, ..., Z=25)
            cipher += chr(((a * p + b) % 26) + 65)  # Apply formula and convert back to letter
        else:
            cipher += ch  # Keep non-alphabetic characters as is
    return cipher

# Decrypt cipher using Affine Cipher
def affine_decrypt(cipher, a, b):
    inv = mod_inverse(a)  # Find modular inverse of 'a'
    if inv is None:
        return "Error: 'a' has no modular inverse"
    
    plain = ""
    for ch in cipher:
        if ch.isalpha():  # Only decrypt letters
            c = ord(ch) - 65  # Convert letter to number
            plain += chr((inv * (c - b)) % 26 + 65)  # Apply decryption formula
        else:
            plain += ch  # Keep non-alphabetic characters as is
    return plain

# Test the cipher
original_text = "HELLO"
a = 5
b = 8

encrypted = affine_encrypt(original_text, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print(f"Original Text: {original_text}")
print(f"Encrypted Text: {encrypted}")
print(f"Decrypted Text: {decrypted}")
