def cesar_crypt(word, decalage):
    code = []
    for char in word:
        char_code = ord(char)
        new_char = chr(char_code + decalage)
        code.append(new_char)
    return "".join(code)

def cesar_decrypt():
    pass

code = cesar_crypt("VENIVIDIVICI", 3)
print(code)