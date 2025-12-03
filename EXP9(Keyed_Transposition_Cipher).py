# Keyed Transposition Cipher

# Encrypt text using Keyed Transposition Cipher
def keyed_transposition_encrypt(text, key):
    # Create a list to find the order of columns based on key
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Create empty columns (one for each character in key)
    columns = [''] * len(key)
    
    # Fill columns with characters from text (column by column)
    for i, ch in enumerate(text):
        columns[i % len(key)] += ch
    
    # Read columns in the order specified by the key
    cipher = ""
    for index in key_order:
        cipher += columns[index]
    
    return cipher


# Decrypt cipher using Keyed Transposition Cipher
def keyed_transposition_decrypt(cipher, key):
    # Find the order in which columns were arranged
    key_order = sorted(range(len(key)), key=lambda i: key[i])
    
    # Calculate how many characters in each column
    num_cols = len(key)
    num_rows = len(cipher) // num_cols
    extra_chars = len(cipher) % num_cols  # Extra characters for uneven division
    
    # Determine length of each column
    col_lengths = [num_rows + 1 if i < extra_chars else num_rows for i in range(num_cols)]
    
    # Extract each column from cipher text
    columns = [''] * num_cols
    start = 0
    for index in key_order:
        col_len = col_lengths[index]
        columns[index] = cipher[start:start + col_len]
        start += col_len
    
    # Read characters row by row to get original text
    result = ""
    for row in range(num_rows + 1):
        for col in range(num_cols):
            if row < len(columns[col]):
                result += columns[col][row]
    
    return result


# Test the cipher
original_text = "HELLOWORLD"
key = "4312"

encrypted = keyed_transposition_encrypt(original_text, key)
decrypted = keyed_transposition_decrypt(encrypted, key)

print(f"Original Text: {original_text}")
print(f"Key: {key}")
print(f"Encrypted Text: {encrypted}")
print(f"Decrypted Text: {decrypted}")

