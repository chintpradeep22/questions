def rail_fence_encrypt(text, rails):
    fence = [["\n"] * len(text) for _ in range(rails)]
    row, down = 0, False
    for i, char in enumerate(text):
        fence[row][i] = char
        if row == 0 or row == rails-1: down = not down
        row += 1 if down else -1
    return "".join("".join(row) for row in fence).replace("\n", "")

def rail_fence_decrypt(cipher, rails):
    fence = [["\n"] * len(cipher) for _ in range(rails)]
    row, down = 0, None
    for i in range(len(cipher)):
        fence[row][i] = "*"
        if row == 0: down = True
        elif row == rails-1: down = False
        row += 1 if down else -1
    idx = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == "*" and idx < len(cipher):
                fence[r][c] = cipher[idx]; idx += 1
    result, row, down = "", 0, None
    for i in range(len(cipher)):
        result += fence[row][i]
        if row == 0: down = True
        elif row == rails-1: down = False
        row += 1 if down else -1
    return result

# Example
cipher = rail_fence_encrypt("HELLO WORLD", 3)
print("Encrypted:", cipher)
print("Decrypted:", rail_fence_decrypt(cipher, 3))
