# Python3 program to implement Hill Cipher

# Initialize matrices
keyMatrix = [[0] * 3 for _ in range(3)]
messageVector = [[0] for _ in range(3)]
cipherMatrix = [[0] for _ in range(3)]


# Function to generate the key matrix from key string
def getKeyMatrix(key: str):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1


# Function to encrypt the message
def encrypt(messageVector: list):
    for i in range(3):
        cipherMatrix[i][0] = 0
        for x in range(3):
            cipherMatrix[i][0] += keyMatrix[i][x] * messageVector[x][0]
        cipherMatrix[i][0] %= 26


# Function to implement Hill Cipher
def HillCipher(message: str, key: str):
    # Generate key matrix
    getKeyMatrix(key)

    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Encrypt the message
    encrypt(messageVector)

    # Convert encrypted vector into ciphertext
    cipherText = [chr(cipherMatrix[i][0] + 65) for i in range(3)]

    print("Ciphertext:", "".join(cipherText))


# Driver code
def main():
    message = "ACT"
    key = "GYBNQKURP"
    HillCipher(message, key)


if __name__ == "__main__":
    main()



# Python3 program to implement Hill Cipher (Encryption + Decryption)
import numpy as np

# Convert key string to key matrix
def getKeyMatrix(key: str) -> np.ndarray:
    keyMatrix = [[0] * 3 for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return np.array(keyMatrix)


# Encryption function
def encrypt(message: str, keyMatrix: np.ndarray) -> str:
    messageVector = [[ord(message[i]) % 65] for i in range(3)]
    messageVector = np.array(messageVector)

    cipherMatrix = np.dot(keyMatrix, messageVector) % 26
    cipherText = "".join(chr(int(cipherMatrix[i][0]) + 65) for i in range(3))
    return cipherText


# Function to find modular inverse of determinant
def modInverse(a: int, m: int) -> int:
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


# Decryption function
def decrypt(cipherText: str, keyMatrix: np.ndarray) -> str:
    cipherVector = [[ord(cipherText[i]) % 65] for i in range(3)]
    cipherVector = np.array(cipherVector)

    # Compute determinant and adjoint of key matrix
    det = int(round(np.linalg.det(keyMatrix))) % 26
    detInv = modInverse(det, 26)

    if detInv == -1:
        raise ValueError("Key matrix is not invertible under mod 26")

    # Compute inverse of key matrix modulo 26
    keyMatrixInv = (
        detInv * np.round(det * np.linalg.inv(keyMatrix)).astype(int)
    ) % 26

    plainMatrix = np.dot(keyMatrixInv, cipherVector) % 26
    plainText = "".join(chr(int(plainMatrix[i][0]) + 65) for i in range(3))
    return plainText


# Driver code
def main():
    message = "ACT"
    key = "GYBNQKURP"

    keyMatrix = getKeyMatrix(key)

    cipherText = encrypt(message, keyMatrix)
    print("Ciphertext:", cipherText)

    plainText = decrypt(cipherText, keyMatrix)
    print("Decrypted Text:", plainText)


if __name__ == "__main__":
    main()

