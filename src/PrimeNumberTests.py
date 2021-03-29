import random
import math
from .Utils import Utils

class PrimeNumberTests:

    @staticmethod
    def solovayStrassenTest(number: int, tests_count: int) -> bool:
        for _ in range(tests_count):
            a = random.randint(1, number - 1)
            jacabi = Utils.jacabiChar(a, number); 
            if jacabi < 1:
                jacabi += number
            
            if not (Utils.gcd(number, a) == 1 and Utils.fastModuloPow(a, (number - 1) // 2, number) == jacabi):
                return False

        return True;

    @staticmethod
    def millerRobinTest(number: int, tests_count: int) -> bool:
        """ Вероятностный тест Миллера-Робина """

        if number == 2 or number == 3:
            return True
        if number <= 1 or number % 2 == 0:
            return False

        s = 0
        r = number - 1
        while r & 1 == 0:
            s += 1
            r //= 2

        for _ in range(tests_count):
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

    def simpleIsPrimeTest(number: int) -> bool:
        """ Простой тест на простое число """

        for i in range(1, int(math.sqrt(number))):
            if number % i == 0:
                return False
        
        return True