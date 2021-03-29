import click
from src.RSAKeyGenerator import RSAKeyGenerator

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
@click.option('-i', '--input-file', 'input_file', default=None, help='Input text file')
@click.option('-o', '--output-file', 'output_file', default=None, help='Output text file')
def encrypt(input_file, output_file):
    """Encrypt text with RSA algorithm"""

if __name__ == '__main__':
    rsa()
