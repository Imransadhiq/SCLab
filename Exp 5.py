from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv, cipher.encrypt(pad(data.encode(), AES.block_size))

def decrypt(iv, ciphertext, key):
    return unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext), AES.block_size).decode()

if __name__ == "__main__":
    key = get_random_bytes(16)
    data = "This is a secret message."

    iv, ciphertext = encrypt(data, key)
    print(f"Ciphertext: {ciphertext.hex()}")

    decrypted_data = decrypt(iv, ciphertext, key)
    print(f"Decrypted: {decrypted_data}")
