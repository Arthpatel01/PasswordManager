import datetime
import os.path

from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, key=None):
        if not key:
            self.__key = self.new_key()
            print("New Secret Key:", self.__key, '\n')
        else:
            self.__key = key

    def new_key(self):
        """
        Generate new secret key for the encryption and decryption of the data.
        :return: Secret Key
        """
        return Fernet.generate_key()

    def encrypt_data(self, secret_key, data):
        """
        Encrypt data using secret key.
        :param secret_key: User's secret key that will be use for encrypt and decrypt the data.
        :param data: Data that you want to encrypt.
        :return: encrypted data
        """
        cipher_suit = Fernet(secret_key)
        encrypted_data = cipher_suit.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, secret_key, encrypted_data):
        """
        Decrypt encrypted data with same secret-key used in encryption.
        :param secret_key: User's same secret-key that used for encryption.
        :param encrypted_data: User's encrypted data.
        :return: encrypted data
        """
        cipher_suit = Fernet(secret_key)
        decrypted_data = cipher_suit.decrypt(encrypted_data).decode()
        return decrypted_data

    def encrypt_file(self, secret_key, file_path):
        """
        This method is responsible for encrypting a file using the given secret_key.
        :param secret_key: The secret key to be used for encryption.
        :param file_path: The path to the file that needs to be encrypted.
        :return: None
        """
        with open(file_path, 'r') as file:
            data = file.read()

        encrypted_data = self.encrypt_data(secret_key=secret_key, data=data)

        # saving in temp_files folder
        with open(file_path + '.encrypted', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        # saving in enc_files folder
        timestep = datetime.datetime.now().timestamp()
        with open('enc_files/' + str(timestep) + '.encrypted', 'wb') as enc_file:
            enc_file.write(encrypted_data)
        "File Encrypted Successfully!"

    def decrypt_file(self, secret_key, file_path):
        """
         This method is responsible for decrypting a file using the given secret_key.
        :param secret_key: The secret key to be used for decryption.
        :param file_path: The path to the file that needs to be decrypted.
        :return: None
        """
        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = self.decrypt_data(secret_key=secret_key, encrypted_data=encrypted_data)

        # Check if the file has either ".enc" or ".encrypted" extension
        if file_path.endswith(".enc"):
            decrypted_file_path = file_path[:-4]
        elif file_path.endswith(".encrypted"):
            decrypted_file_path = file_path[:-10]
        else:
            print("Error: Invalid file extension.")
            return

        with open(decrypted_file_path, 'w') as decrypted_file:
            decrypted_file.write(decrypted_data)
        "File Decrypted Successfully!"

    def engine(self):
        """
        This method provides a user interface for interacting with the
        """
        try:
            while True:
                print("""
                Please choose any one option:
                1 - Encrypt File
                2 - Decrypt File
                """)
                option = input("Please enter any number from above: ")

                if option == "1":
                    """User want file encryption"""
                    print("\n\nMake sure you have pasted the file you want to encrypt inside temp_files")
                    while True:
                        filename = input("Enter file name with extension (e.g., myfile.txt): ")
                        file_path = f'./temp_files/{filename}'

                        if not os.path.exists(file_path):
                            print(f'File "{file_path}" not found.')
                            continue
                        else:
                            self.encrypt_file(secret_key=self.__key, file_path=file_path)
                            print('File Encrypted Successfully!')
                            return

                elif option == "2":
                    """User wants file decryption"""
                    print("\n\nMake sure you have pasted the file you want to decrypt inside temp_files")
                    while True:
                        filename = input("Enter file name with extension (e.g., myfile.txt.encrypted): ")
                        file_path = f'./temp_files/{filename}'
                        if not os.path.exists(file_path):
                            print(f"File '{file_path}' not found.")
                            continue
                        else:
                            self.decrypt_file(secret_key=self.__key, file_path=file_path)
                            print("File Decrypted Successfully!")
                            return

                else:
                    print("Invalid option. Please choose either 1 or 2.")
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    key_file_path = r""
    if key_file_path:
        with open(key_file_path, 'r') as kf:
            key = kf.read()
        kf.close()
    else:
        key = ""

    p = PasswordManager(key=key)
    p.engine()
