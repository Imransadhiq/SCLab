def encrypt_text(plaintext, n):
    ans = ""
    for ch in plaintext:
        if ch.isalpha():
            if ch.isupper():
                ans += chr((ord(ch) + n - 65) % 26 + 65)
            elif ch.islower():
                ans += chr((ord(ch) + n - 97) % 26 + 97)
        elif ch.isdigit():
            ans += chr((ord(ch) + n - 48) % 10 + 48)
        else:
            ans += chr((ord(ch) + n) % 128)
    return ans

def decrypt_text(ciphertext, n):
    ans = ""
    for ch in ciphertext:
        if ch.isalpha():
            if ch.isupper():
                ans += chr((ord(ch) - n - 65) % 26 + 65)
            elif ch.islower():
                ans += chr((ord(ch) - n - 97) % 26 + 97)
        elif ch.isdigit():
            ans += chr((ord(ch) - n - 48) % 10 + 48)
        else:
            ans += chr((ord(ch) - n) % 128)
    return ans

plaintext = "99220040600@klu.ac.in"
n = 3
ciphertext = encrypt_text(plaintext, n)
decrypted_text = decrypt_text(ciphertext, n)
print("plain text is : ", plaintext)
print("shift value is :", n)
print("cipher text is : ", ciphertext)
print("decrypted text is : ", decrypted_text)