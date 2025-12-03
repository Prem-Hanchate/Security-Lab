# Rail Fence Cipher

def rail_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    row = 0
    step = 1

    for char in text:
        fence[row].append(char)
        if row == 0: step = 1
        elif row == rails - 1: step = -1
        row += step

    return "".join("".join(row) for row in fence)

print(rail_encrypt("HELLOWORLD", 3))


def rail_decrypt(cipher, rails):
    pattern = []
    row = 0
    step = 1

    for _ in cipher:
        pattern.append(row)
        if row == 0: step = 1
        elif row == rails-1: step = -1
        row += step

    fence = [""] * len(cipher)
    index = 0

    for r in range(rails):
        for i in range(len(cipher)):
            if pattern[i] == r:
                fence[i] = cipher[index]
                index += 1

    result = ""
    row = 0
    step = 1
    for i in range(len(cipher)):
        result += fence[i]
    return result

print(rail_decrypt(rail_encrypt("HELLOWORLD", 3), 3))

