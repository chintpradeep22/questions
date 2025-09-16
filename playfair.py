import numpy as np

def generate_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # remove duplicates
    matrix = list(key + "".join([chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != "J"]))
    return np.array(matrix).reshape(5, 5)

def find_pos(matrix, char):
    char = "I" if char == "J" else char
    x, y = np.where(matrix == char)
    return x[0], y[0]

def playfair_encrypt(text, matrix):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0: text += "X"
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        ax, ay = find_pos(matrix, a)
        bx, by = find_pos(matrix, b)
        if ax == bx:
            result += matrix[ax][(ay+1)%5] + matrix[bx][(by+1)%5]
        elif ay == by:
            result += matrix[(ax+1)%5][ay] + matrix[(bx+1)%5][by]
        else:
            result += matrix[ax][by] + matrix[bx][ay]
    return result

def playfair_decrypt(cipher, matrix):
    result = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        ax, ay = find_pos(matrix, a)
        bx, by = find_pos(matrix, b)
        if ax == bx:
            result += matrix[ax][(ay-1)%5] + matrix[bx][(by-1)%5]
        elif ay == by:
            result += matrix[(ax-1)%5][ay] + matrix[(bx-1)%5][by]
        else:
            result += matrix[ax][by] + matrix[bx][ay]
    return result

# Example
matrix = generate_key_matrix("KEYWORD")
cipher = playfair_encrypt("HELLO", matrix)
print("Encrypted:", cipher)
print("Decrypted:", playfair_decrypt(cipher, matrix))
