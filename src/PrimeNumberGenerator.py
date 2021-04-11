from random import randrange, getrandbits
from .PrimeNumberTests import PrimeNumberTests
import math


class PrimeNumberGenerator:
    def __init__(self, length=None, tests_count=None):
        self.tests_count = length if tests_count is None else tests_count
        self.length = 1024 if length is None else length

    def isPrime(self, number: int) -> bool:
        return PrimeNumberTests.millerRobinTest(number, self.tests_count)

    def generatePrimeCandidate(self):
        """ Сгенерировать случайное нечетное число длинной self.length бит """

        number = getrandbits(self.length)
        # Применить маску для установки MSB и LSB в 1
        number |= (1 << self.length - 1) | 1
        return number

    def getPrime(self):
        """ Сгенерировать простое число длинной self.length бит """

        prime = 4
        while not self.isPrime(prime):
            prime = self.generatePrimeCandidate()
        return prime

    def getPrimes(self, count=1):
        """ Сгенерировать count простых чисел длинной self.length бит """

        primes = []
        for _ in range(count):
            primes.append(self.getPrime())
        return primes
