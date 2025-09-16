def caesar(text, shift):
  result = ""
  for ch in text:
    if ch.islower():
      result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
      result += chr((ord(ch) - 65 + shift) % 26 + 65)
  return result
plain  = "HELLO"
shift=int(input("enter shift value : "))
enc    = caesar(plain, shift)    # Encrypt with shift = +3
dec    = caesar(enc,  -shift)    # Decrypt by using -35
print("Plain Text :", plain)
print("Encrypted Text :", enc)
print("Decrypted Text :", dec)
