def cesar(word, decalage, crypt) -> str:
    code = []
    for char in word:
        char_code = ord(char)
        if crypt:
            new_char = chr(char_code + decalage)
        else:
            new_char = chr(char_code - decalage)
        code.append(new_char)
    return "".join(code)

def cesar_crypt(word, decalage) -> str:
    return cesar(word, decalage, True)

def cesar_decrypt(word, decalage) -> str:
    return cesar(word, decalage, False)

code = cesar_crypt("VENIVIDIVICI", 3)
print(code)
code = cesar_decrypt(code, 3)
print(code)