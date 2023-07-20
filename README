# PasswordManager

PasswordManager is a Python class that provides encryption and decryption capabilities for files using the Fernet encryption scheme from the `cryptography` library.

## Requirements

- Python 3.x
- `cryptography` library

## Usage

1. Import necessary modules:

```python
import datetime
import os.path
from cryptography.fernet import Fernet
```

2. Create an instance of the `PasswordManager` class:

```python
# Provide the secret key or leave it empty to generate a new key
p = PasswordManager(key=b'your_secret_key')
```

3. Use the `encrypt_file` and `decrypt_file` methods to encrypt and decrypt files, respectively:

```python
# Encrypt a file
p.encrypt_file(secret_key=your_secret_key, file_path='path/to/file')

# Decrypt a file
p.decrypt_file(secret_key=your_secret_key, file_path='path/to/encrypted_file')
```

4. Use the `engine` method to interact with the PasswordManager through the console:

```python
p.engine()
```

## Method Details

### `new_key()`

Generate a new secret key for encryption and decryption of data.

### `encrypt_data(secret_key, data)`

Encrypt the provided data using the given secret key.

### `decrypt_data(secret_key, encrypted_data)`

Decrypt the encrypted data using the given secret key.

### `encrypt_file(secret_key, file_path)`

Encrypt a file using the provided secret key.

### `decrypt_file(secret_key, file_path)`

Decrypt an encrypted file using the provided secret key.

### `engine()`

Interactive user interface to choose file encryption or decryption.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The `cryptography` library for providing the Fernet encryption implementation.

Feel free to modify and use this template for your project. Happy coding!

# PasswordManager

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PasswordManager is a Python class that provides encryption and decryption capabilities for files using the Fernet encryption scheme from the `cryptography` library.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

```bash
pip install cryptography
Usage
Import necessary modules:
python
Copy code
import datetime
import os.path
from cryptography.fernet import Fernet
Create an instance of the PasswordManager class:
python
Copy code
# Provide the secret key or leave it empty to generate a new key
p = PasswordManager(key=b'your_secret_key')
Use the encrypt_file and decrypt_file methods to encrypt and decrypt files, respectively:
python
Copy code
# Encrypt a file
p.encrypt_file(secret_key=your_secret_key, file_path='path/to/file')

# Decrypt a file
p.decrypt_file(secret_key=your_secret_key, file_path='path/to/encrypted_file')
Use the engine method to interact with the PasswordManager through the console:
python
Copy code
p.engine()
Method Details
new_key()
Generate a new secret key for encryption and decryption of data.

encrypt_data(secret_key, data)
Encrypt the provided data using the given secret key.

decrypt_data(secret_key, encrypted_data)
Decrypt the encrypted data using the given secret key.

encrypt_file(secret_key, file_path)
Encrypt a file using the provided secret key.

decrypt_file(secret_key, file_path)
Decrypt an encrypted file using the provided secret key.

engine()
Interactive user interface to choose file encryption or decryption.

Contributions
Contributions to this project are welcome! If you find a bug or have suggestions for improvement, please feel free to create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
The cryptography library for providing the Fernet encryption implementation.