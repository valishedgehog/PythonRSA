# PythonRSA
Python 3 RSA algorithm implementation

## Usage

- Get help message
```
python3 rsa.py --help
```

- Generate rsa public and private keys
Example of generation 2048 bit keys in ```./keys/key.pub``` and ```./keys/key``` files
```
python3 rsa.py generate-key -l 2048 -o ./keys/key
```

- Encrypt text with generated private key
Keys are located in folder ```./keys```, ```input.txt``` - input text, ```crypt_text.txt``` - encrypted text file
```
python.exe rsa.py encrypt -i input.txt -o crypt_text.txt -k ./keys/key
```

- Decrypt text with generated private key
Keys are located in folder ```./keys```, ```crypt_text.txt``` - input encrypted text, ```output.txt``` - decrypted text file
```
python.exe rsa.py decrypt -i crypt_text.txt -o output.txt -k ./keys/key
```
