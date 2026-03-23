import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_set = set(alphabet)

def decode(text: str, key: str) -> str:

    decoded_chars: list[str] = []
    for index, char in enumerate(text):
        if char not in alphabet_set:
            decoded_chars.append(char)
        else:
            char_index = alphabet.index(char)
            key_char = key[(index) % len(key)]
            key_index = alphabet.index(key_char)

            decoded_chars.append(
                alphabet[(char_index - key_index) % len(alphabet)]
            )

    return "".join(decoded_chars)

def discover_key(text: str) -> str:
    characters = {}
    for character in text:
        if character in alphabet_set:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    most_common_char = max(characters, key=characters.get)
    key_char = alphabet[(alphabet.index(most_common_char) - alphabet.index('E')) % len(alphabet)]
    return key_char


with open(os.path.join(os.path.dirname(__file__), "crypted_vigenere.txt"), "r") as file:
    ciphertext = file.read().strip()

key = discover_key(ciphertext)
code = decode(ciphertext, "DELICIEUX")
print(f"Discovered key: {key}")
# print(f"Decrypted message: {code}")