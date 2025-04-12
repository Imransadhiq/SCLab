from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys
key = RSA.generate(2048)
private_key, public_key = key.export_key(), key.publickey().export_key()

# Save keys to files
for name, data in [("private.pem", private_key), ("public.pem", public_key)]:
    with open(name, 'wb') as f:
        f.write(data)

def sign_message(message, private_key):
    h = SHA256.new(message.encode())
    return pkcs1_15.new(RSA.import_key(private_key)).sign(h)

def verify_signature(message, signature, public_key):
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(RSA.import_key(public_key)).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    message = "This is a secret message."
    signature = sign_message(message, private_key)
    print(f"Signature: {signature.hex()}")
    print(f"Signature valid: {verify_signature(message, signature, public_key)}")
