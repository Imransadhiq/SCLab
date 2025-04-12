def generate_cipher_key(shift): 
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] 
    return dict(zip(alphabet, shifted_alphabet)) 

def encrypt(message, key): 
    encrypted_message = '' 
    for char in message: 
        if char.isalpha(): 
            encrypted_message += key[char.lower()].upper() if char.isupper() else key[char] 
        else: 
            encrypted_message += char 
    return encrypted_message 

def decrypt(ciphertext, key): 
    reverse_key = {v: k for k, v in key.items()} 
    decrypted_message = '' 
    for char in ciphertext: 
        if char.isalpha(): 
            decrypted_message += reverse_key[char.lower()].upper() if char.isupper() else reverse_key[char] 
        else: 
            decrypted_message += char 
    return decrypted_message 

def main(): 
    shift = int(input("Enter the shift value for the cipher: ")) 
    key = generate_cipher_key(shift) 
    choice = input("Encrypt or decrypt? (e/d): ").lower() 
    if choice == 'e': 
        print("Encrypted message:", encrypt(input("Enter the message to encrypt: "), key)) 
    elif choice == 'd': 
        print("Decrypted message:", decrypt(input("Enter the message to decrypt: "), key)) 
    else: 
        print("Invalid choice.") 

if __name__ == "__main__": 
    main()
