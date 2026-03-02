def cesar(word, decalage, crypt) -> str:
    code = []
    for char in word:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char_code = ord(char) - base
            if crypt:
                new_char = chr((char_code + decalage) % 26 + base)
            else:
                new_char = chr((char_code - decalage) % 26 + base)
            code.append(new_char)
        else:
            code.append(char)
    return "".join(code)

def cesar_crypt(word, decalage) -> str:
    return cesar(word, decalage, True)

def cesar_decrypt(word, decalage) -> str:
    return cesar(word, decalage, False)

code = cesar_crypt("VENIVIDIVICI", 3)
print(code)
code = cesar_decrypt(code, 3)
print(code)

def count_letters(word):
    alphabet = {}
    for char in word:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet

def discover_decalage(word):
    alphabet = count_letters(word)
    most_common_letter = max(alphabet, key=alphabet.get)
    decalage = ord(most_common_letter) - ord('E')
    return decalage

print(discover_decalage("AVJLZJRCREKLIZEXZEMVEKVLIDVTFEELULKVJKUVKLIZEX"))

for i in range(26):
    print(f"Décalage {i}: {cesar_decrypt('AVJLZJRCREKLIZEXZEMVEKVLIDVTFEELULKVJKUVKLIZEX', i)}")

print(cesar_decrypt("AVJLZJRCREKLIZEXZEMVEKVLIDVTFEELULKVJKUVKLIZEX", 17))