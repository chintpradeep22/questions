def hex2bin(s):
    """Convert hex string to binary string with zero padding."""
    return bin(int(s, 16))[2:].zfill(len(s) * 4)


def bin2hex(s):
    """Convert binary string to hex string with zero padding."""
    return hex(int(s, 2))[2:].upper().zfill(len(s) // 4)


def permute(k, arr):
    """Permute string `k` based on indices in `arr` (1-indexed)."""
    return "".join(k[i - 1] for i in arr)


def xor(a, b):
    """Bitwise XOR between two binary strings."""
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))


# Minimal S-box: Example values (4 S-boxes, 4x4)
sbox = [
    [[14, 4, 13, 1], [2, 15, 11, 8], [3, 10, 6, 12], [5, 9, 0, 7]],
    [[15, 1, 8, 14], [6, 11, 3, 4], [9, 7, 2, 13], [12, 0, 5, 10]],
    [[10, 0, 9, 14], [6, 3, 15, 5], [1, 13, 12, 7], [11, 4, 2, 8]],
    [[7, 13, 14, 3], [0, 6, 9, 10], [1, 2, 8, 5], [11, 12, 4, 15]]
]

# Simplified permutations (identity)
initial_perm = list(range(1, 33))
final_perm = list(range(1, 33))


def sbox_substitute(inp):
    """Perform substitution using the defined S-box."""
    out = ''
    for i in range(4):
        block = inp[i * 4:(i + 1) * 4]
        row = int(block[0] + block[3], 2)
        col = int(block[1:3], 2)
        val = sbox[i][row][col]
        out += bin(val)[2:].zfill(4)
    return out


def encrypt(pt, round_keys):
    """Encrypt plaintext using simplified Feistel structure."""
    pt = hex2bin(pt)
    pt = permute(pt, initial_perm)

    left, right = pt[:16], pt[16:]
    print(f"Initial L0: {bin2hex(left)}, R0: {bin2hex(right)}")

    for i, rk in enumerate(round_keys):
        # Normally right is expanded, skipping for simplicity
        xored = xor(right, rk)
        sbox_out = sbox_substitute(xored[:16])  # Simplified: only 16 bits
        new_right = xor(left, sbox_out)

        left, right = right, new_right
        print(f"After round {i + 1}: L{i + 1}: {bin2hex(left)}, R{i + 1}: {bin2hex(right)}")

    combined = left + right
    cipher = permute(combined, final_perm)
    return cipher


# --- Main Program ---
if __name__ == "__main__":
    # Using a fixed 16-bit round key repeated 16 times
    round_keys = [bin(int('1334', 16))[2:].zfill(16)] * 16

    pt = input("Enter plaintext (8 hex chars): ").upper()
    ct = encrypt(pt, round_keys)
    print("Ciphertext:", bin2hex(ct))
