from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_message(message):
    if not os.path.exists("secret.key"):
        key = generate_key()
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(message.encode())

    with open("encrypted_data.txt", "wb") as enc_file:
        enc_file.write(encrypted_data)

    print("Encryption Successful!")

def decrypt_message():
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()

        with open("encrypted_data.txt", "rb") as enc_file:
            encrypted_data = enc_file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        print("Decryption Successful!")
        print("Original Message:", decrypted_data.decode())

    except FileNotFoundError:
        print("Required files not found.")
    except:
        print("Invalid Key or Corrupted Data!")

if __name__ == "__main__":
    choice = input("Enter 1 to Encrypt, 2 to Decrypt: ")

    if choice == "1":
        message = input("Enter text to encrypt: ")
        encrypt_message(message)
    elif choice == "2":
        decrypt_message()
    else:
        print("Invalid choice")
