def rail_fence_encrypt(text, rails):
    """Encrypts text using the Rail Fence Cipher."""
    if rails <= 1:
        return text

    # Create a list of strings, one for each rail
    fence = [''] * rails
    current_rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in text:
        # Add the character to the current rail's string
        fence[current_rail] += char
        
        # If we reach the top or bottom rail, reverse direction
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
            
        # Move to the next rail
        current_rail += direction

    # Join all the rail strings to get the final encrypted message
    return "".join(fence)


def rail_fence_decrypt(cipher, rails):
    """Decrypts text from the Rail Fence Cipher."""
    if rails <= 1:
        return cipher

    # 1. Figure out the length of each rail
    rail_lengths = [0] * rails
    current_rail = 0
    direction = 1
    for _ in cipher:
        rail_lengths[current_rail] += 1
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction

    # 2. Rebuild the rails by slicing the ciphertext
    fence = []
    index = 0
    for length in rail_lengths:
        fence.append(list(cipher[index : index + length]))
        index += length

    # 3. Read the rails in zigzag order to get the original text
    result = []
    current_rail = 0
    direction = 1
    for _ in cipher:
        # Get the next letter from the correct rail
        result.append(fence[current_rail].pop(0))
        
        # Change direction at the top or bottom
        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1
        current_rail += direction

    return "".join(result)

# Example
original_text = "HELLO WORLD"
num_rails = 3

encrypted_text = rail_fence_encrypt(original_text, num_rails)
print(f"Encrypted: {encrypted_text}")

decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
print(f"Decrypted: {decrypted_text}")
