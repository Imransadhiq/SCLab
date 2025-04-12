from math import gcd

def RSA(p: int, q: int, message: int):
    n = p * q
    t = (p - 1) * (q - 1)

    e = next(i for i in range(2, t) if gcd(i, t) == 1)

    d = next(j for j in range(1, t) if (j * e) % t == 1)

    ct = pow(message, e, n)
    print(f"Encrypted message: {ct}")

    mes = pow(ct, d, n)
    print(f"Decrypted message: {mes}")

RSA(53, 59, 89)
RSA(3, 7, 12)
