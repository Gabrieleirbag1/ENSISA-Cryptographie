import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file_cbc(input_file: str, output_file: str, key_file: str):
    key = get_random_bytes(32)

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    # Pad the plaintext to be a multiple of AES block size (16 bytes)
    padded_plaintext = pad(plaintext, AES.block_size)

    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the IV and ciphertext to output file
    # IV is needed for decryption and is stored at the beginning
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)  # Write IV (16 bytes)
        f.write(ciphertext)  # Write encrypted data

    with open(key_file, 'wb') as f:
        f.write(key)

    print(f"File encrypted successfully!")
    print(f"Encrypted file: {output_file}")
    print(f"Key saved to: {key_file}")


def decrypt_file_cbc(input_file: str, output_file: str, key_file: str):
    with open(key_file, 'rb') as f:
        key = f.read()

    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Read the IV (first 16 bytes)
        ciphertext = f.read()  # Read the rest (encrypted data)

    # Create AES cipher in CBC mode with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    padded_plaintext = cipher.decrypt(ciphertext)

    # Remove padding
    plaintext = unpad(padded_plaintext, AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted successfully!")
    print(f"Decrypted file: {output_file}")


def decrypt_secrets_jpg():
    key = b'\x97N2\xcb\xf615i\x1b\xb6qs\xf6\xe2\x9d\xdb'

    input_file = os.path.join(os.path.dirname(__file__), "secrets.jpg")
    output_file = os.path.join(os.path.dirname(__file__), "secrets_decrypted.jpg")

    with open(input_file, 'rb') as f:
        nonce = f.read(8)  # Read the 8-byte nonce
        ciphertext = f.read()  # Read the rest (encrypted data)

    # Create AES cipher in CTR mode with the nonce
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

    # Decrypt (CTR mode doesn't need padding/unpadding)
    plaintext = cipher.decrypt(ciphertext)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"secrets.jpg decrypted successfully!")
    print(f"Decrypted file: {output_file}")


script_dir = os.path.dirname(__file__)

print("Task 1: Encrypting poeme.txt with AES CBC")
encrypt_file_cbc(
    input_file=os.path.join(script_dir, "poeme.txt"),
    output_file=os.path.join(script_dir, "poeme_encrypted.bin"),
    key_file=os.path.join(script_dir, "poeme_key.bin")
)

print("\nTask 2: Decrypting poeme_encrypted.bin with AES CBC")
decrypt_file_cbc(
    input_file=os.path.join(script_dir, "poeme_encrypted.bin"),
    output_file=os.path.join(script_dir, "poeme_decrypted.txt"),
    key_file=os.path.join(script_dir, "poeme_key.bin")
)

print("\nTask 3: Decrypting secrets.jpg with AES CTR")
decrypt_secrets_jpg()
