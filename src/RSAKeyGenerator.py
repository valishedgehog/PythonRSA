from .PrimeNumberGenerator import PrimeNumberGenerator
import random
import os

class RSAKeyGenerator:
    def __init__(self, length=None, output_file=None):
        self.length = 1024 if length is None else length
        self.output_file = 'key' if output_file is None else output_file

        self.length = self.length // 2
        self.prime_generator = PrimeNumberGenerator(length=self.length, tests_count=128)

    def generate(self) -> None:
        p, q = self.prime_generator.getPrimes(2)
        n, phi = p * q, (p - 1) * (q - 1)
        public_key = self.getPublicKey(n)
        private_key = self.extendedGcd(phi, public_key)[0]

        self.saveKeys(public_key, private_key)

    def getPublicKey(self, n: int) -> int:
        e = None
        while e is None or RSAKeyGenerator.gcd(e, n) != 1:
            e = random.randint(2, n)

        return e

    def getPrivateKey(self, phi, public_key):
        return RSAKeyGenerator.extendedGcd(phi, public_key)[0]

    def saveKeys(self, publicKey: int, privateKey: int) -> None:
        if not os.path.exists(os.path.dirname(self.output_file)):
            try:
                os.makedirs(os.path.dirname(self.output_file))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        with open(self.output_file + '.pub', 'w') as output:
            output.write(str(publicKey))
        with open(self.output_file, 'w') as output:
            output.write(str(privateKey))

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while a != b:
            if a > b:
                a, b = b, a
            b = b - a
        return a
    
    @staticmethod
    def extendedGcd(a: int, b: int):
        x, xx, y, yy = 1, 0, 0, 1
        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx*q
            y, yy = yy, y - yy*q
        return (x, y, a)


