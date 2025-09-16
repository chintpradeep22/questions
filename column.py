def columnar_trans_encrypt(plaintext, key, padchar='X'):
    m = len(key)
    rows = -(-len(plaintext)//m)
    padded = plaintext + padchar * (rows*m - len(plaintext))
    matrix = [list(padded[i*m:(i+1)*m]) for i in range(rows)]
    order = sorted(range(m), key=lambda k: (key[k], k))
    return "".join(matrix[r][col] for col in order for r in range(rows))

def columnar_trans_decrypt(ciphertext, key, padchar='X'):
    m = len(key)
    rows = -(-len(ciphertext)//m)
    matrix = [['']*m for _ in range(rows)]
    order = sorted(range(m), key=lambda k: (key[k], k))
    idx = 0
    for col in order:
        for r in range(rows):
            matrix[r][col] = ciphertext[idx]; idx += 1
    plain = "".join(''.join(row) for row in matrix)
    return plain.rstrip(padchar)

# example
pt = "HELLOWORLD"
k = "4312"
ct = columnar_trans_encrypt(pt, k)
print(ct)
print(columnar_trans_decrypt(ct, k))
