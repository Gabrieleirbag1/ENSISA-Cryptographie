import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TD2.test_primalité_fermat import fermat_test
import random

def crypt(m, e, N):
    c = pow(m, e, N)

    print(f"Encrypted message: c = {c}")
    return c

def decrypt(c, d, N):
    m = pow(c, d, N)
    print(f"Decrypted message: m = {m}")
    decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, "big").decode()
    print(f"Decrypted message (string): {decrypted_message}")

def main():
    p, q = None, None
    e = 65537  # Common choice for e
    
    import math
    while not p or not q:
        # Increase the range to ensure N > m so the message doesn't overflow
        random_number = random.randint(10**6, 10**8)
        if fermat_test(random_number):
            if not p and math.gcd(random_number - 1, e) == 1:
                p = random_number
            elif not q and p != random_number and math.gcd(random_number - 1, e) == 1:
                q = random_number
    print(f"Found primes: p = {p}, q = {q}")

    m = input("Enter a message to encrypt: ")
    m = int.from_bytes(m.encode("utf-8"), "big")
    print(f"Message to encrypt: m = {m}")

    N = p * q
    phi_N = (p - 1) * (q - 1)

    d = pow(e, -1, phi_N)

    print(f"Public key: (N={N}, e={e})")
    print(f"Private key: (N={N}, d={d})")
    
    c = crypt(m, e, N)
    decrypt(c, d, N)

if __name__ == "__main__":
    main()
