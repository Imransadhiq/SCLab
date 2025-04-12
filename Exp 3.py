import hashlib  

text = "GeeksforGeeks"

print("The hexadecimal equivalent of SHA256 is:", hashlib.sha256(text.encode()).hexdigest())  
print("The hexadecimal equivalent of SHA384 is:", hashlib.sha384(text.encode()).hexdigest())  
print("The hexadecimal equivalent of SHA224 is:", hashlib.sha224(text.encode()).hexdigest())  
print("The hexadecimal equivalent of SHA512 is:", hashlib.sha512(text.encode()).hexdigest())  
print("The hexadecimal equivalent of SHA1 is:", hashlib.sha1(text.encode()).hexdigest())  
