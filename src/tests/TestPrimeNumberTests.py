from src.PrimeNumberTests import PrimeNumberTests
from src.PrimeNumberGenerator import PrimeNumberGenerator
from TestDecorator import benchmark

DELIMETER = "==============================================="
TESTS_COUNT = 100
NUMBERS_COUNT = 10
LENGTH_LIST = [8, 16, 32, 128, 512, 1024]

class TestPrimeNumberTests:
    @benchmark
    def test(self, numbers: list, test_func: callable) -> None:
        for number in numbers:
            test_func(number, TESTS_COUNT)


    def run(self) -> None:
        test_functions = {
            'Simple': PrimeNumberTests.simpleIsPrimeTest,
            'Solovay-Strassen': PrimeNumberTests.solovayStrassenTest,
            'Miller-Robin': PrimeNumberTests.millerRobinTest
        }

        for length in LENGTH_LIST:
            print(DELIMETER)
            generator = PrimeNumberGenerator(length=length)
            numbers = generator.getPrimes(NUMBERS_COUNT)
            print("Start test with {} number of length {} bit".format(NUMBERS_COUNT, length))
            for test_name, test_func in test_functions.items():
                print("Testing with {} test".format(test_name))
                self.test(numbers, test_func)
            
if __name__ == '__main__':
    test = TestPrimeNumberTests()
    test.run()

            


