def is_prime(n):
    """Test de primalité naïf."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test du code
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 15, 17, 19, 20, 23, 25]
    for num in test_numbers:
        if is_prime(num):
            print(f"{num} est premier.")
        else:
            print(f"{num} est composé.")