from random import randrange, getrandbits
import math


class PrimeNumberGenerator:
    def __init__(self, length=None, tests_count=None):
        self.tests_count = 128 if tests_count is None else tests_count
        self.length = 1024 if length is None else length

    def isPrime(self, number: int) -> bool:
        """ Проверить число на простое вероятностным тестом Миллера-Робина """

        if number == 2 or number == 3:
            return True
        if number <= 1 or number % 2 == 0:
            return False

        s = 0
        r = number - 1
        while r & 1 == 0:
            s += 1
            r //= 2

        for _ in range(self.tests_count):
            a = randrange(2, number - 1)
            x = pow(a, r, number)
            if x != 1 and x != number - 1:
                j = 1
                while j < s and x != number - 1:
                    x = pow(x, 2, number)
                    if x == 1:
                        return False
                    j += 1
                if x != number - 1:
                    return False

        return True

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
