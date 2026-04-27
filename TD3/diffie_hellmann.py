import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TD2.test_primalité_miller import miller_rabin_test
import random

def main():
    p = None
    while not p:
        random_number = random.randint(1, 10**6)
        print(f"Testing if {random_number} is prime using Miller-Rabin test...")
        if miller_rabin_test(random_number):
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

if __name__ == "__main__":
    main()