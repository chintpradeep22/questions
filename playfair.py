def generate_key_matrix(key):
    """Creates the 5x5 key matrix for the Playfair cipher."""
    # 1. Prepare the key: uppercase, replace J with I, remove duplicates
    key = key.upper().replace("J", "I")
    unique_key_chars = ""
    for char in key:
        if char not in unique_key_chars:
            unique_key_chars += char

    # 2. Build the rest of the matrix with the remaining alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    char_sequence = unique_key_chars
    for char in alphabet:
        if char not in char_sequence:
            char_sequence += char
            
    # 3. Convert the sequence into a 5x5 grid (list of lists)
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(char_sequence[i:i+5]))
    return matrix

def prepare_plaintext(text, pad_char='X'):
    """Prepares text for encryption: creates pairs, handles double letters."""
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        prepared_text += char1
        i += 1
        
        # If we are at the end of the text
        if i == len(text):
            prepared_text += pad_char
            break
            
        char2 = text[i]
        # If the characters are the same, add a padding char
        if char1 == char2:
            prepared_text += pad_char
        else:
            prepared_text += char2
            i += 1
            
    return prepared_text

def find_position(matrix, char):
    """Finds the (row, col) of a character in the matrix."""
    for r, row_list in enumerate(matrix):
        for c, character in enumerate(row_list):
            if character == char:
                return r, c
    return -1, -1 # Should not happen with valid input

def playfair_transform(text, matrix, direction):
    """A single function to encrypt or decrypt based on the direction."""
    # direction: 1 for encrypt (move right/down), -1 for decrypt (move left/up)
    output = ""
    
    # Process the text in pairs of characters (digraphs)
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2: # Rule 1: Same row
            output += matrix[r1][(c1 + direction) % 5]
            output += matrix[r2][(c2 + direction) % 5]
        elif c1 == c2: # Rule 2: Same column
            output += matrix[(r1 + direction) % 5][c1]
            output += matrix[(r2 + direction) % 5][c2]
        else: # Rule 3: Rectangle
            output += matrix[r1][c2]
            output += matrix[r2][c1]
            
    return output

# --- Main Functions ---
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_plaintext(plaintext)
    return playfair_transform(prepared_text, matrix, 1)

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    return playfair_transform(ciphertext, matrix, -1)


# Example
keyword = "KEYWORD"
plaintext = "HELLO WORLD"

ciphertext = playfair_encrypt(plaintext, keyword)
print(f"Encrypted: {ciphertext}")

decrypted_text = playfair_decrypt(ciphertext, keyword)
print(f"Decrypted: {decrypted_text}")
