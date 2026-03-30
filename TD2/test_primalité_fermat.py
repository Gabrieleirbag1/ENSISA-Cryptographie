#EXERCICE 6
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

def fermat_test(n: int, k: int = 5) -> bool:
    """Effectue le test de primalité de Fermat sur n avec k itérations."""
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(k):
        a = randint(2, n - 2)  # Choisir un entier aléatoire entre 2 et n-2
        if power_mod(a, n - 1, n) != 1:
            return False  # n est composé
    return True  # n est probablement premier

# Test du code
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 15, 17, 19, 20, 23, 25]
    for num in test_numbers:
        if fermat_test(num):
            print(f"{num} est probablement premier.")
        else:
            print(f"{num} est composé.")