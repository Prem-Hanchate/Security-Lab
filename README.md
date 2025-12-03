# 🔐 Security Lab - Cryptography Implementations

A comprehensive collection of classical and modern cryptography cipher implementations in Python. This repository contains practical implementations of various encryption and decryption techniques used in information security.

## 📚 Table of Contents

- [Introduction](#introduction)
- [Cipher Implementations](#cipher-implementations)
  - [Substitution Ciphers](#substitution-ciphers)
  - [Transposition Ciphers](#transposition-ciphers)
  - [Modern Cryptography](#modern-cryptography)
- [How to Run](#how-to-run)
- [Concepts Explained](#concepts-explained)

---

## 🎯 Introduction

This repository contains implementations of 11 different cryptographic ciphers, ranging from simple classical ciphers to modern public-key cryptography. Each implementation is written in Python with clear, easy-to-understand code and comments.

**What is Cryptography?**  
Cryptography is the practice of securing information by transforming it into an unreadable format (encryption) and then back to readable format (decryption). Only those with the correct key can decrypt the message.

---

## 🔑 Cipher Implementations

### Substitution Ciphers
These ciphers replace each letter with another letter or symbol.

#### 1. Caesar Cipher (EXP1)
**What it does:** Shifts each letter in the message by a fixed number of positions in the alphabet.

**How it works:**
- Choose a shift value (e.g., 3)
- Move each letter forward by that many positions
- Example: "HELLO" with shift 3 → "KHOOR"
- A becomes D, B becomes E, and so on

**Use case:** One of the oldest and simplest encryption techniques, used by Julius Caesar.

---

#### 2. Additive Cipher (EXP2)
**What it does:** Similar to Caesar Cipher - adds a key value to each letter's position.

**How it works:**
- Convert each letter to a number (A=0, B=1, ..., Z=25)
- Add the key to each number
- Apply modulo 26 to wrap around
- Convert back to letters

**Use case:** Basic encryption for understanding modular arithmetic in cryptography.

---

#### 3. Shift Cipher (EXP3)
**What it does:** Another name for Caesar Cipher - shifts letters by a fixed amount.

**How it works:**
- Same principle as Caesar Cipher
- Encryption: E(x) = (x + k) mod 26
- Decryption: D(x) = (x - k) mod 26
- Where k is the shift key

**Use case:** Educational purposes to understand basic substitution.

---

#### 4. Multiplicative Cipher (EXP4)
**What it does:** Multiplies each letter's position by a key value.

**How it works:**
- Convert letter to number (A=0, B=1, ..., Z=25)
- Multiply by the key
- Apply modulo 26
- Convert back to letter
- **Important:** Key must be coprime with 26 (share no common factors)

**Example:** With key 5, letter C (2) → (2 × 5) mod 26 = 10 → K

**Use case:** Slightly more secure than additive ciphers.

---

#### 5. Affine Cipher (EXP5)
**What it does:** Combines both multiplicative and additive ciphers.

**How it works:**
- Uses two keys: 'a' (multiplicative) and 'b' (additive)
- Encryption: E(x) = (a × x + b) mod 26
- Decryption: D(x) = a⁻¹ × (x - b) mod 26
- Requires finding modular inverse of 'a'

**Example:** With a=5, b=8, letter H (7) → (5×7+8) mod 26 = 17 → R

**Use case:** More secure combination of two cipher techniques.

---

#### 6. Autokey Cipher (EXP6)
**What it does:** Uses the message itself as part of the key.

**How it works:**
- Start with an initial key letter
- Add the first letter of the message to create the next key
- Continue using plaintext as the key stream
- Each letter encrypted with a different key

**Example:** 
- Message: "HELLO", Key: "K"
- Extended key: "KHELL"
- Each position uses different shift

**Use case:** Improves security by using a changing key.

---

#### 7. Vigenère Cipher (EXP7)
**What it does:** Uses a keyword to encrypt - each letter of the keyword shifts the corresponding message letter.

**How it works:**
- Choose a keyword (e.g., "KEY")
- Repeat the keyword to match message length
- Each letter uses a different shift based on keyword position
- Much harder to break than Caesar Cipher

**Example:**
- Message: "HELLO", Key: "KEY"
- H+K, E+E, L+Y, L+K, O+E
- Result: "RIJVS"

**Use case:** Used for centuries, considered unbreakable until frequency analysis was developed.

---

### Transposition Ciphers
These ciphers rearrange the letters without changing them.

#### 8. Rail Fence Cipher (EXP8)
**What it does:** Writes the message in a zigzag pattern across multiple rails (rows).

**How it works:**
- Write message diagonally across specified number of rails
- Read off each rail from top to bottom
- Example with 3 rails:
  ```
  H . . . O . . . L .
  . E . L . W . R . D
  . . L . . . O . . .
  ```
- Result: "HOLELWRDLO"

**Use case:** Simple transposition for basic message scrambling.

---

#### 9. Keyed Transposition Cipher (EXP9)
**What it does:** Rearranges message columns based on a numeric key.

**How it works:**
- Write message in rows under a keyword
- Number columns based on alphabetical order of keyword
- Read columns in the order specified by numbers
- Example:
  ```
  Key: 4312
  H E L L
  O W O R
  L D
  ```
- Read columns in order: 3,1,2,4 → "LOLREWDHOL"

**Use case:** Military and diplomatic communications.

---

### Modern Cryptography

#### 10. Hill Cipher (EXP10)
**What it does:** Uses matrix multiplication for encryption (linear algebra).

**How it works:**
- Convert message to number vectors
- Multiply by a key matrix
- Apply modulo 26
- Convert back to letters
- Requires matrix inverse for decryption

**Use case:** First cipher to use linear algebra, foundation for modern cryptography.

---

#### 11. RSA Encryption (EXP15)
**What it does:** Modern public-key cryptography - uses two keys (public and private).

**How it works:**
1. Choose two prime numbers (p, q)
2. Calculate n = p × q
3. Calculate φ(n) = (p-1) × (q-1)
4. Choose public exponent e
5. Calculate private exponent d (modular inverse of e)
6. Public key: (e, n), Private key: (d, n)
7. Encryption: C = M^e mod n
8. Decryption: M = C^d mod n

**Example:**
- p=11, q=13 → n=143, φ=120
- e=7, d=103
- Message 9 → Encrypted: 48 → Decrypted: 9

**Use case:** Secure online communications, HTTPS, digital signatures, cryptocurrency.

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Running Individual Ciphers

```bash
# Navigate to the directory
cd "Security Lab Practical's"

# Run any cipher implementation
python EXP1(Caesar_Cipher).py
python EXP5(Affine_Cipher).py
python EXP15(RSA_Encryption_and_Decryption).py
```

---

## 📖 Concepts Explained

### 🔤 Substitution vs Transposition

- **Substitution Ciphers:** Replace letters with other letters/symbols
  - Examples: Caesar, Vigenère, Affine, RSA
  - Maintains letter positions but changes the letters
  
- **Transposition Ciphers:** Rearrange letter positions
  - Examples: Rail Fence, Keyed Transposition
  - Keeps original letters but changes their order

### 🔢 Modular Arithmetic

Many ciphers use "mod 26" (remainder when divided by 26):
- Ensures results stay within alphabet (0-25 or A-Z)
- Example: 28 mod 26 = 2 (wraps around to C)

### 🔐 Symmetric vs Asymmetric Encryption

- **Symmetric (Same key for encryption & decryption):**
  - All classical ciphers (Caesar, Vigenère, etc.)
  - Fast but key sharing is a problem
  
- **Asymmetric (Different keys - public & private):**
  - RSA
  - Slower but solves key distribution problem
  - Foundation of modern internet security

### 🎯 Cryptanalysis (Breaking Ciphers)

- **Frequency Analysis:** Analyzing letter frequency to break substitution ciphers
- **Brute Force:** Trying all possible keys
- **Known Plaintext Attack:** Using known message-cipher pairs

---

## 📝 Key Takeaways

1. **Classical ciphers** (Caesar, Vigenère) are educational but not secure for modern use
2. **Transposition ciphers** scramble but don't hide letter frequencies
3. **RSA** is the foundation of modern internet security
4. **Key management** is crucial - even strong ciphers fail with weak keys
5. **Layering** multiple cipher techniques increases security

---

## 🎓 Learning Path

1. Start with **Caesar Cipher** - understand basic substitution
2. Move to **Vigenère Cipher** - see how changing keys improves security
3. Try **Rail Fence** - understand transposition concept
4. Study **Affine Cipher** - learn about mathematical operations
5. Finally **RSA** - understand modern public-key cryptography

---

## 🤝 Contributing

Feel free to fork this repository and add more cipher implementations or improvements!

---

## 📄 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

**Prem Hanchate**

Created as part of Security Lab Practicals for understanding cryptographic concepts.

---

## 🌟 Star this repo if you found it helpful!

Happy Learning! 🎉
