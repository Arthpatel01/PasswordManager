# PasswordManager

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

PasswordManager is licensed under the MIT License. By contributing to this project, you agree to release your contributions under this license.

We look forward to your contributions and hope you find the project enjoyable to work on!

Feel free to modify this section to better suit your project's specific contribution guidelines and community practices. Happy coding!


## Developers

If you are a developer interested in contributing to PasswordManager, we welcome your contributions! Whether it's fixing bugs, adding new features, or improving documentation, your help is valuable.

### Contributing

To contribute to the project, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your changes.
3. Make your changes and commit them with descriptive commit messages.
4. Push your branch to your forked repository.
5. Create a pull request (PR) against the `main` branch of the original repository.

### Issues and Bug Reports

If you find any issues or bugs in the PasswordManager project, please create an issue on GitHub. Include detailed information about the problem, steps to reproduce it, and any relevant error messages.

### Code of Conduct

We expect all contributors to adhere to the project's [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and considerate of others while participating in the project.
