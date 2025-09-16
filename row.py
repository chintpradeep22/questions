def row_trans_encrypt(plaintext, key, padchar='X'):
    m = len(key)
    rows = [plaintext[i:i+m] for i in range(0, len(plaintext), m)]
    if len(rows[-1]) < m:
        rows[-1] += padchar * (m - len(rows[-1]))
    order = sorted(range(m), key=lambda k: (key[k], k))
    return "".join("".join(row[order[i]] for i in range(m)) for row in rows)

def row_trans_decrypt(ciphertext, key, padchar='X'):
    m = len(key)
    cipher_rows = [ciphertext[i:i+m] for i in range(0, len(ciphertext), m)]
    order = sorted(range(m), key=lambda k: (key[k], k))
    plain = ""
    for crow in cipher_rows:
        row = [''] * m
        for i, ch in enumerate(crow):
            row[order[i]] = ch
        plain += "".join(row)
    return plain.rstrip(padchar)

# example
pt = "HELLOWORLD"
k = "4312"
ct = row_trans_encrypt(pt, k)
print(ct)
print(row_trans_decrypt(ct, k))
