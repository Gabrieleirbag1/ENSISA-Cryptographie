#test de primalité de Miller-Rabin --- IGNORE ---
from random import randint

def power_mod(base: int, exp: int, mod: int) -> int:
    """Calcul de (base^exp) mod mod en utilisant l'exponentiation rapide."""
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # Si exp est impair, multiplie la base par le résultat
            result = (result * base) % mod
        exp = exp >> 1  # Divise exp par 2
        base = (base * base) % mod  # Multiplie la base par elle-même
    return result

def miller_rabin_test(n: int, k: int = 5) -> bool:
    """Effectue le test de primalité de Miller-Rabin sur n avec k itérations."""
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Écrire n-1 comme d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = randint(2, n - 2)  # Choisir un entier aléatoire entre 2 et n-2
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n est composé
    return True  # n est probablement premier

# Test du code
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 15, 17, 19, 20, 23, 25]
    for num in test_numbers:
        if miller_rabin_test(num):
            print(f"{num} est probablement premier.")
        else:
            print(f"{num} est composé.")