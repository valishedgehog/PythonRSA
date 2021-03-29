from .PrimeNumberGenerator import PrimeNumberGenerator
from .Utils import Utils
import random


class RSAKeyGenerator:
    def __init__(self, length=None, output_file=None):
        self.length = 1024 if length is None else length
        self.output_file = 'key' if output_file is None else output_file

        self.length = self.length // 2
        self.prime_generator = PrimeNumberGenerator(length=self.length)

    def generate(self) -> None:
        p, q = self.prime_generator.getPrimes(2)
        n, phi = p * q, (p - 1) * (q - 1)
        public_key = self.getPublicKey(phi)
        private_key = self.getPrivateKey(phi, public_key)
        self.saveKeys(public_key, private_key, n)

    def getPublicKey(self, n: int) -> int:
        e = None
        while e is None or Utils.gcd(e, n) != 1:
            e = random.randint(2, n - 1)
        return e

    def getPrivateKey(self, phi, public_key):
        result = Utils.extendedGcd(phi, public_key)[1] % phi
        return Utils.extendedGcd(phi, public_key)[1] % phi

    def saveKeys(self, publicKey: int, privateKey: int, n: int) -> None:
        Utils.createFoldersInPath(self.output_file)
        with open(self.output_file + '.pub', 'w') as output:
            output.write(str(publicKey) + '\n')
            output.write(str(n) + '\n')
        with open(self.output_file, 'w') as output:
            output.write(str(privateKey) + '\n')
            output.write(str(n) + '\n')
