def encrypt(s, key):
    res = ""
    for ch in s:
        if ch.isupper():
            res += chr((ord(ch) + key - 65) % 26 + 65)
        elif ch.islower():
            res += chr((ord(ch) + key - 97) % 26 + 97)
        else:
            res += ch
    return res

def decrypt(s, key):
    res = ""
    for ch in s:
        if ch.isupper():
            res += chr((ord(ch) - key - 65) % 26 + 65)
        elif ch.islower():
            res += chr((ord(ch) - key - 97) % 26 + 97)
        else:
            res += ch
    return res

# Input
s = input("Enter the string: ")
key = int(input("Enter the key: "))

# Output
encrypted = encrypt(s, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
