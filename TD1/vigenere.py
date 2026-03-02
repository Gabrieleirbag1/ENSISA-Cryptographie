class Mathys():
    pass


def set_alphabet_matrice() -> Mathys:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matrice = []
    for i in range(26):
        row = alphabet[i:] + alphabet[:i]
        matrice.append(row)
    return matrice

matrice = set_alphabet_matrice()

def decrypt(word, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = []
    
    # Extend key to match word length
    extended_key = (key * (len(word) // len(key) + 1))[:len(word)]
    
    for (c, k) in zip(word, extended_key):
        k_pos = alphabet.index(k)
        c_pos = matrice[k_pos].index(c)
        code.append(alphabet[c_pos])
    
    return ''.join(code)

code = decrypt("DIXFSHEWYVZRLKMEIKMBUZDSFSCMCOKSAJSX", "LACRYPTOGRAPHIECESTLAVIE")
print(code)