import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0: text += "X"
    result = ""
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        enc = np.dot(key, pair) % 26
        result += "".join(chr(x+65) for x in enc.flatten())
    return result

def hill_decrypt(cipher, key):
    det = int(np.round(np.linalg.det(key))) % 26
    inv_det = pow(det, -1, 26)
    key_inv = (inv_det * np.round(det * np.linalg.inv(key)).astype(int)) % 26
    result = ""
    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]])
        dec = np.dot(key_inv, pair) % 26
        result += "".join(chr(int(x)+65) for x in dec.flatten())
    return result

# Example
key = np.array([[3, 3], [2, 5]])
cipher = hill_encrypt("HELLO", key)
print("Encrypted:", cipher)
print("Decrypted:", hill_decrypt(cipher, key))
