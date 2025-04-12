from Crypto.Cipher import DES

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].upper().zfill(len(bin_str) // 4)

def permute(block, table):
    return ''.join(block[i - 1] for i in table)

def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def s_box_substitution(block, s_boxes):
    output = ''
    for i in range(8):
        row = int(block[i * 6] + block[i * 6 + 5], 2)
        col = int(block[i * 6 + 1:i * 6 + 5], 2)
        output += bin(s_boxes[i][row][col])[2:].zfill(4)
    return output

def left_shift(key, shifts):
    return key[shifts:] + key[:shifts]

def generate_keys(key):
    pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    key = permute(hex_to_bin(key), pc1)
    left, right = key[:28], key[28:]
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    keys = []
    for shift in shifts:
        left, right = left_shift(left, shift), left_shift(right, shift)
        keys.append(permute(left + right, pc2))
    return keys

def encrypt(block, keys):
    ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    inv_ip = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    block = permute(hex_to_bin(block), ip)
    left, right = block[:32], block[32:]
    expansion = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    for key in keys:
        temp = xor(permute(right, expansion), key)
        right = xor(left, temp)
        left = temp
    return bin_to_hex(permute(right + left, inv_ip))

key = "133457799BBCDFF1"
plaintext = "0123456789ABCDEF"
keys = generate_keys(key)
ciphertext = encrypt(plaintext, keys)
print("Ciphertext:", ciphertext)
