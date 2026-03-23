import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Task 1: Encrypt poeme.txt using AES with CBC mode
def encrypt_file_cbc(input_file: str, output_file: str, key_file: str):
    """
    Encrypts a file using AES in CBC mode.
    Saves the key and IV to a file for later decryption.
    """
    # Generate a random 256-bit (32 bytes) key
    key = get_random_bytes(32)

    # Read the input file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    # Pad the plaintext to be a multiple of AES block size (16 bytes)
    padded_plaintext = pad(plaintext, AES.block_size)

    # Encrypt
    ciphertext = cipher.encrypt(padded_plaintext)

    # Write the IV and ciphertext to output file
    # IV is needed for decryption and is stored at the beginning
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)  # Write IV (16 bytes)
        f.write(ciphertext)  # Write encrypted data

    # Save the key to a separate file
    with open(key_file, 'wb') as f:
        f.write(key)

    print(f"File encrypted successfully!")
    print(f"Encrypted file: {output_file}")
    print(f"Key saved to: {key_file}")


# Task 2: Decrypt a file encrypted with AES CBC
def decrypt_file_cbc(input_file: str, output_file: str, key_file: str):
    """
    Decrypts a file that was encrypted using AES in CBC mode.
    Reads the key from the key file.
    """
    # Read the key
    with open(key_file, 'rb') as f:
        key = f.read()

    # Read the encrypted file
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Read the IV (first 16 bytes)
        ciphertext = f.read()  # Read the rest (encrypted data)

    # Create AES cipher in CBC mode with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Decrypt
    padded_plaintext = cipher.decrypt(ciphertext)

    # Remove padding
    plaintext = unpad(padded_plaintext, AES.block_size)

    # Write the decrypted data to output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted successfully!")
    print(f"Decrypted file: {output_file}")


# Task 3: Decrypt secrets.jpg encrypted with AES CTR mode
def decrypt_secrets_jpg():
    """
    Decrypts the secrets.jpg file that was encrypted with AES in CTR mode.
    The file has an 8-byte nonce at the beginning.
    """
    # Given key
    key = b'\x97N2\xcb\xf615i\x1b\xb6qs\xf6\xe2\x9d\xdb'

    input_file = os.path.join(os.path.dirname(__file__), "secrets.jpg")
    output_file = os.path.join(os.path.dirname(__file__), "secrets_decrypted.jpg")

    # Read the encrypted file
    with open(input_file, 'rb') as f:
        nonce = f.read(8)  # Read the 8-byte nonce
        ciphertext = f.read()  # Read the rest (encrypted data)

    # Create AES cipher in CTR mode with the nonce
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

    # Decrypt (CTR mode doesn't need padding/unpadding)
    plaintext = cipher.decrypt(ciphertext)

    # Write the decrypted image
    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"secrets.jpg decrypted successfully!")
    print(f"Decrypted file: {output_file}")


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    print("=" * 60)
    print("Task 1: Encrypting poeme.txt with AES CBC")
    print("=" * 60)
    encrypt_file_cbc(
        input_file=os.path.join(script_dir, "poeme.txt"),
        output_file=os.path.join(script_dir, "poeme_encrypted.bin"),
        key_file=os.path.join(script_dir, "poeme_key.bin")
    )

    print("\n" + "=" * 60)
    print("Task 2: Decrypting poeme_encrypted.bin with AES CBC")
    print("=" * 60)
    decrypt_file_cbc(
        input_file=os.path.join(script_dir, "poeme_encrypted.bin"),
        output_file=os.path.join(script_dir, "poeme_decrypted.txt"),
        key_file=os.path.join(script_dir, "poeme_key.bin")
    )

    print("\n" + "=" * 60)
    print("Task 3: Decrypting secrets.jpg with AES CTR")
    print("=" * 60)
    try:
        decrypt_secrets_jpg()
    except FileNotFoundError:
        print("Error: secrets.jpg not found in the TD1 directory")
        print("Please make sure the file exists before running task 3")
