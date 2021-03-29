import click
import os

from src.RSAKeyGenerator import RSAKeyGenerator
from src.RSACryptor import RSACryptor


@click.group()
def rsa():
    pass


@rsa.command()
@click.option('-l', '--length', 'length', default=2048, help='Bit length of key')
@click.option('-o', '--output-file', 'output_file', default='key', help='File where to generate keys')
def generate_key(length, output_file):
    """ Generate rsa public and private keys of given bits length """

    key_generator = RSAKeyGenerator(length=length, output_file=output_file)
    key_generator.generate()


@rsa.command()
@click.option('-i', '--input-file', 'input_file', default=None, help='Input text file', required=True)
@click.option('-o', '--output-file', 'output_file', default=None, help='Output text file', required=True)
@click.option('-k', '--key', 'key_file', default=None, help='Key file location', required=True)
def encrypt(input_file, output_file, key_file):
    """Encrypt text with RSA algorithm"""

    if not os.path.isfile(input_file):
        print("Can not find input file {}".format(input_file))
        return

    if not os.path.isfile(key_file):
        print("Can not find private key file {}".format(key_file))
        return

    if not os.path.isfile(input_file):
        print("Can not find output file {}".format(output_file))
        return

    RSACryptor(input_file, output_file, key_file).encrypt()


@rsa.command()
@click.option('-i', '--input-file', 'input_file', default=None, help='Input text file', required=True)
@click.option('-o', '--output-file', 'output_file', default=None, help='Output text file', required=True)
@click.option('-k', '--key', 'key_file', default=None, help='Private key file location', required=True)
def decrypt(input_file, output_file, key_file):
    """Decrypt text with RSA algorithm"""

    if not os.path.isfile(input_file):
        print("Can not find input file {}".format(input_file))
        return

    key_file = key_file.replace('.pub', '')
    if not os.path.isfile(key_file + '.pub'):
        print("Can not find public key file {}".format(key_file + '.pub'))
        return

    if not os.path.isfile(input_file):
        print("Can not find output file {}".format(output_file))
        return

    RSACryptor(input_file, output_file, key_file + '.pub').decrypt()


if __name__ == '__main__':
    rsa()
