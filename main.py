import csv
import datetime
import os.path
import platform
import subprocess

from colorama import Fore, Style

from cryptography.fernet import Fernet


class EncryptionManager:
    def __init__(self, key=None):
        if not key:
            self.__key = self.new_key()
            print(Fore.GREEN + "New Secret Key:", self.__key.decode() + Style.RESET_ALL, '\n')
        else:
            self.__key = key

    def new_key(self):
        """
        Generate a new secret key for the encryption and decryption of the data.
        :return: Secret Key
        """
        return Fernet.generate_key()

    def encrypt_data(self, secret_key, data):
        """
        Encrypt data using the secret key.
        :param secret_key: User's secret key that will be used for encryption and decryption of the data.
        :param data: Data that you want to encrypt.
        :return: Encrypted data
        """
        try:
            cipher_suit = Fernet(secret_key)
            encrypted_data = cipher_suit.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            print(Fore.RED + 'Error during data encryption:', e, Style.RESET_ALL)

    def decrypt_data(self, secret_key, encrypted_data):
        """
        Decrypt encrypted data with the same secret-key used in encryption.
        :param secret_key: User's secret key that used for encryption.
        :param encrypted_data: User's encrypted data.
        :return: Decrypted data
        """
        try:
            cipher_suit = Fernet(secret_key)
            decrypted_data = cipher_suit.decrypt(encrypted_data).decode()
            return decrypted_data
        except Exception as e:
            print(Fore.RED + "Error during data decryption:", e, Style.RESET_ALL)
            return None

    def encrypt_file(self, secret_key, file_path):
        """
        Encrypt a file using the given secret_key.
        :param secret_key: The secret key to be used for encryption.
        :param file_path: The path to the file that needs to be encrypted.
        :return: None
        """
        try:
            with open(file_path, 'r') as file:
                data = file.read()

            encrypted_data = self.encrypt_data(secret_key=secret_key, data=data)

            # Saving in temp_files folder
            with open(file_path + '.encrypted', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            # Saving in enc_files folder
            timestep = datetime.datetime.now().timestamp()

            # Check if the folder does not exist, then create it first
            self.exist_or_create_directory('./enc_files')
            with open('enc_files/' + str(timestep) + '.encrypted', 'wb') as enc_file:
                enc_file.write(encrypted_data)

        except Exception as e:
            print(Fore.RED + "Error during file encryption:", e, Style.RESET_ALL)

    def decrypt_file(self, secret_key, file_path):
        """
        Decrypt a file using the given secret_key.
        :param secret_key: The secret key to be used for decryption.
        :param file_path: The path to the file that needs to be decrypted.
        :return: None
        """
        try:
            with open(file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = self.decrypt_data(secret_key=secret_key, encrypted_data=encrypted_data)

            # Check if the file has either ".enc" or ".encrypted" extension
            if decrypted_data is not None:
                if file_path.endswith(".enc"):
                    decrypted_file_path = file_path[:-4]
                elif file_path.endswith(".encrypted"):
                    decrypted_file_path = file_path[:-10]
                else:
                    print(Fore.RED + "Error: Invalid file extension." + Style.RESET_ALL)
                    return

                with open(decrypted_file_path, 'w') as decrypted_file:
                    decrypted_file.write(decrypted_data)
            else:
                print(Fore.RED + "File Decryption Failed." + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + "Error during file decryption:", e, Style.RESET_ALL)

    def encrypted_file_data(self, secret_key, path):
        """
        Decrypt file ---> read data ---> decrypt file ---> return data.
        Using this function, we will ensure that the file is not open or decrypted.
        :return: Data from decrypted file.
        """
        pass

    @staticmethod
    def exist_or_create_directory(path):
        """
        This function will check if the given directory (path) is available, if not ---> create it.
        :param path: Directory/Folder path, e.g., ./temp_folder
        :return: None
        """
        try:
            if not os.path.exists(os.path.join(os.getcwd(), path)):
                os.mkdir(os.path.join(os.getcwd(), path))
        except Exception as e:
            print(Fore.RED + 'Error (exist_or_create_directory): ', e, Style.RESET_ALL)

    @staticmethod
    def exist_or_create_file(path, default_data=""):
        """
        Function will create a file if not exist.
        path: file name with full path --> e.g., user/desktop/my_file.txt
        """
        try:
            if not os.path.exists(os.path.join(os.getcwd(), path)):
                with open(path, 'w') as file:
                    if default_data:
                        file.write(default_data)
                    file.close()
        except Exception as e:
            print(Fore.RED + 'Error (exist_or_create_file): ', e, Style.RESET_ALL)


class PasswordManager:
    def __init__(self, key_file_path=None):
        key = self.read_key_from_file(key_file_path)
        self.encryption_manager = EncryptionManager(key=key)
        self.__key = self.encryption_manager._EncryptionManager__key

    def read_key_from_file(self, key_file_path):
        key = None
        try:
            if key_file_path:
                with open(key_file_path, 'rb') as file:
                    key = file.read()
        except Exception as e:
            print(Fore.RED + 'Error (read_key_from_file):', e, Style.RESET_ALL)
        return key

    @staticmethod
    def delete_file(path):
        """Delete the given file"""
        try:
            if os.path.exists(os.path.join(os.getcwd(), path)):
                os.remove(path=path)
        except Exception as e:
            print(Fore.RED + 'Error (delete_file): ', e, Style.RESET_ALL)

    @staticmethod
    def add_new_row_to_csv(file_path, data):
        """
        Add a new row to the CSV file.
        :param file_path: The path to the CSV file.
        :param data: A list containing the data for the new row.
        """
        # Open the CSV file in 'r+' mode to read and write
        with open(file_path, 'r+', newline='') as csv_file:
            # Read the existing data and header (if present)
            rows = list(csv.reader(csv_file))
            header = rows[0] if rows else None

            # Append the new data as a new row
            rows.append(data)

            # Write back to the CSV file
            csv_file.seek(0)  # Move the cursor to the beginning of the file
            csv_writer = csv.writer(csv_file)
            if header and header not in rows:
                csv_writer.writerow(header)  # Write back the header if present and not already added
            csv_writer.writerows(rows)  # Write all rows

    @staticmethod
    def get_column_values(file_path, column_name):
        """
        Get the values of a specific column from the CSV file.
        :param file_path: The path to the CSV file.
        :param column_name: The name of the column whose values you want to retrieve.
        :return: A list containing the values of the specified column.
        """
        column_values = []

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                value = row.get(column_name)
                if value is not None:
                    column_values.append(value)
        return column_values

    def get_new_id_for_csv(self, file_path, column_name):
        new_id = None
        try:
            if file_path and column_name:
                list_ids = self.get_column_values(file_path=file_path, column_name=column_name)
                if list_ids:
                    list_ids = [int(id) for id in list_ids]  # Convert the list of strings to a list of integers
                    biggest_id = max(list_ids)
                    if biggest_id:
                        new_id = int(biggest_id) + 1
                else:
                    if len(list_ids) == 0:
                        new_id = 1
        except Exception as e:
            print(Fore.RED + 'Error (get_new_id_for_csv): ', e, Style.RESET_ALL)
        return new_id

    def pms_add(self, file_path, enc_file_path):
        """
        Function to handle adding a new username and password.
        """
        try:
            # If a new file is created, this data should be in that file for the header.
            default_data = 'ID,Username,Password,Created At,Modified At'

            # Check the file, if it does not exist, then create it.
            if not os.path.exists(os.path.join(os.getcwd(), enc_file_path)):
                self.encryption_manager.exist_or_create_file(file_path, default_data)

            # No matter what, first encrypt secure_credentials.csv if not encrypted.
            try:
                self.encryption_manager.encrypt_file(secret_key=self.__key, file_path=file_path)

                # Delete the simple one after creating the encrypted file.
                self.delete_file(path=file_path)
            except:
                pass

            # Take user input
            print('Adding a new Username and Password')
            un = input('Enter Username:')
            ps = input('Enter Password:')

            # Encrypted file path and decrypt it.
            self.encryption_manager.decrypt_file(secret_key=self.__key, file_path=enc_file_path)

            # Generate a new ID and current-time to add in the CSV
            new_id = self.get_new_id_for_csv(file_path=file_path, column_name="ID")
            current_datetime = datetime.datetime.now()

            # List of user data column-wise as a list [ID,Username,Password,Created At,Modified At]
            data = [new_id, un, ps, current_datetime, '']
            self.add_new_row_to_csv(file_path=file_path, data=data)

            # Encrypt the updated file
            self.encryption_manager.encrypt_file(secret_key=self.__key, file_path=file_path)

            # Remove the original unencrypted file
            self.delete_file(path=file_path)

            print(Fore.GREEN + "New Username and Password added successfully." + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + "Error during adding username and password:", e, Style.RESET_ALL)

    def pms_view(self, enc_file_path):
        """
        View the password data in a formatted table.
        :param enc_file_path: Path to the encrypted password data file.
        """
        try:
            with open(enc_file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            decrypted_data = self.encryption_manager.decrypt_data(secret_key=self.__key, encrypted_data=encrypted_data)
            if not decrypted_data:
                print(Fore.YELLOW + "No password data found." + Style.RESET_ALL)
                return

            # Convert the decrypted data from CSV format to a list of dictionaries
            data = []
            csv_reader = csv.DictReader(decrypted_data.splitlines())
            for row in csv_reader:
                data.append(row)

            # Convert the data to a list to avoid the iterator exhaustion issue
            data = list(data)

            # Print the data in a formatted table
            headers = csv_reader.fieldnames

            # Calculate the maximum width of each column
            column_widths = []
            for col in csv_reader.fieldnames:
                max_width = 0
                for item in data:
                    width = len(str(item.get(col, '')))
                    if width > max_width:
                        max_width = width
                column_widths.append(max_width)

            header_row = " | ".join(headers[i].ljust(column_widths[i]) for i in range(len(headers)))
            separator = "-" * len(header_row)
            print(header_row)
            print(separator)
            for item in data:
                row = " | ".join(str(item.get(col, '')).ljust(column_widths[i]) for i, col in enumerate(headers))
                print(row.rstrip())
        except Exception as e:
            print(Fore.RED + "Error during viewing password data:", e, Style.RESET_ALL)

    def pms(self):
        """This function will handle pms(add passwords, view passwords)"""
        try:
            # Check the data directory, if not exist, then create it
            folder_path = './data'
            self.encryption_manager.exist_or_create_directory(folder_path)
            file_path = folder_path + '/secure_credentials.csv'
            enc_file_path = file_path + '.encrypted'

            while True:
                print("""
                                Please choose any one option:
                                1 - Add New Username and Password
                                2 - View All Usernames and Passwords
                                3 - Back
                                """)
                option = input("Please enter any number from above: ")

                if option == '1':
                    self.pms_add(file_path, enc_file_path)
                elif option == '2':
                    self.pms_view(enc_file_path)
                elif option == '3':
                    break
                else:
                    print(Fore.RED + 'Invalid Option. Please choose either 1, 2, or 3.' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Error during password management:", e, Style.RESET_ALL)

    def engine(self):
        """
        This method provides a user interface for interacting with the program.
        """
        try:
            while True:
                print("\n\n")
                print(Fore.CYAN + r"""
______                                   _  ___  ___                                  
| ___ \                                 | | |  \/  |                                  
| |_/ /_ _ ___ _____      _____  _ __ __| | | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |   
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                       __/ |          
                                                                      |___/                  
                        by Arth Patel

                """ + Style.RESET_ALL)
                print("""
                Please choose any one option:
                1 - Password Manager
                2 - Encrypt File
                3 - Decrypt File
                e - Exit
                """)
                option = input("Please enter any number from above: ")

                if option == "1":
                    """Password Manager System PMS"""
                    self.pms()
                elif option == "2":
                    """User wants file encryption"""
                    print("\n\nMake sure you have pasted the file you want to encrypt inside temp_files")
                    while True:
                        filename = input("Enter the file name with extension (e.g., myfile.txt): ")
                        file_path = f'./temp_files/{filename}'

                        if not os.path.exists(file_path):
                            print(Fore.RED + f'File "{file_path}" not found.' + Style.RESET_ALL)
                            continue
                        else:
                            self.encryption_manager.encrypt_file(secret_key=self.__key, file_path=file_path)
                            print(Fore.GREEN + 'File Encrypted Successfully!' + Style.RESET_ALL)
                            return

                elif option == "3":
                    """User wants file decryption"""
                    print("\n\nMake sure you have pasted the file you want to decrypt inside temp_files")
                    while True:
                        filename = input("Enter the file name with extension (e.g., myfile.txt.encrypted): ")
                        file_path = f'./temp_files/{filename}'
                        if not os.path.exists(file_path):
                            print(Fore.RED + f"File '{file_path}' not found." + Style.RESET_ALL)
                            continue
                        else:
                            self.encryption_manager.decrypt_file(secret_key=self.__key, file_path=file_path)
                            print(Fore.GREEN + "File Decrypted Successfully!" + Style.RESET_ALL)
                            return
                elif option.lower() == 'e':
                    """Exit From Program"""
                    return
                else:
                    print(Fore.RED + "Invalid option. Please choose either 1, 2, or 3." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Error in the main engine:", e, Style.RESET_ALL)


if __name__ == '__main__':
    key_file_path = r"C:\Users\PMS\Desktop\sk-202307194.txt"

    try:
        p = PasswordManager(key_file_path=key_file_path)
        if platform.system() == 'Windows':
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)
        p.engine()
    except Exception as e:
        print(Fore.RED + "Error in the main program:", e, Style.RESET_ALL)
