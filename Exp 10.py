import hashlib

def compute_hash(data):
    """Computes SHA-256 hash of the given data."""
    return hashlib.sha256(data.encode()).hexdigest()

def verify_integrity(data1, data2):
    """Verifies integrity by comparing hashes of two messages."""
    hash1 = compute_hash(data1)
    hash2 = compute_hash(data2)

    print(f"Hash of first data: {hash1}")
    print(f"Hash of second data: {hash2}")

    if hash1 == hash2:
        print("Integrity Verified: The data is identical.")
    else:
        print("Integrity Check Failed: The data is modified.")

# Example usage
message1 = input("Enter first message: ")
message2 = input("Enter second message: ")

verify_integrity(message1, message2)
