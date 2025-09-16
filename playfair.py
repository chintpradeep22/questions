def clean_text(text):
    return text.replace(" ", "").lower().replace('j', 'i')

def prepare_plaintext(text):
    if len(text) % 2 != 0:
        text += 'z'
    return text

def generate_key_matrix(key):
    key = clean_text(key)
    matrix = []
    used = set()
    for char in key:
        if char not in used and char != 'j':
            matrix.append(char)
            used.add(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in used and char != 'j':
            matrix.append(char)
    key_table = [matrix[i*5:(i+1)*5] for i in range(5)]
    return key_table

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:  # same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # rectangle rule
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:  # same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # rectangle rule
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_playfair(plaintext, key):
    plaintext = clean_text(plaintext)
    plaintext = prepare_plaintext(plaintext)
    matrix = generate_key_matrix(key)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        ciphertext += encrypt_pair(matrix, a, b)
    return ciphertext

def decrypt_playfair(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    matrix = generate_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        plaintext += decrypt_pair(matrix, a, b)
    return plaintext

# Input / Output
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = encrypt_playfair(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")

decrypted = decrypt_playfair(ciphertext, key)
print(f"Decrypted: {decrypted}")
