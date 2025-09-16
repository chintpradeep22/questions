def encrypt_rail_fence(text, rails):
    text = text.replace(" ", "").upper()
    rail = ['' for _ in range(rails)]
    dir_down = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        row += 1 if dir_down else -1

    return ''.join(rail)


def decrypt_rail_fence(cipher, rails):
    n = len(cipher)
    rail = [['\n' for _ in range(n)] for _ in range(rails)]

    dir_down = None
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(rails):
        for j in range(n):
            if rail[i][j] == '*' and index < n:
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        result.append(rail[row][col])
        col += 1
        row += 1 if dir_down else -1

    return ''.join(result)


# --- Simple demo ---
text = input("Enter plain text: ")
num_rails = int(input("Enter number of rails: "))

cipher_text = encrypt_rail_fence(text, num_rails)
decrypted_text = decrypt_rail_fence(cipher_text, num_rails)

print("\nEncrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
