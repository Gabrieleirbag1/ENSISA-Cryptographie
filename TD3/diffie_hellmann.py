import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TD2.test_primalité_fermat import fermat_test
import random

def main():
    p = None
    while not p:
        random_number = random.randint(1, 10**6)
        print(f"Testing if {random_number} is prime using Fermat test...")
        if fermat_test(random_number):
            p = random_number
    print(f"Found prime: p = {p}")

    a = random.randint(1, p-1)
    b = random.randint(1, p-1)

    g = random.randint(1, p-1)

    A = pow(g, a, p)
    B = pow(g, b, p)

    K1 = pow(B, a, p)
    K2 = pow(A, b, p)

    if K1 == K2:
        print(f"Shared secret key successfully computed: K = {K1}")
    else:
        print("Error: Shared secret keys do not match.")

def decrypt(p, g, A, B, c):
    a = 0
    while pow(g, a, p) != A:
        a += 1
    b = 0
    while pow(g, b, p) != B:
        b += 1
    K1 = pow(B, a, p)
    K2 = pow(A, b, p)
    if K1 == K2:
        K = K1
        print(f"Shared secret key successfully computed: K = {K}")

if __name__ == "__main__":
    main()
    print("\n===========================================================")
    decrypt(467, 2, 228, 57, "GRHTTXKRJTHRI")