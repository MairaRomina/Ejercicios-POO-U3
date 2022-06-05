import unittest
from Palindromo import Palindromo


class TestPalindromo(unittest.TestCase):
    __palindromo = None

    def setUp(self):
        self.__palindromo = Palindromo('Menem')

    def testPalindromoPar(self):
        self.assertEqual(self.__palindromo.esPalindromo(), True)

    def testUnNoPalindromo(self):
        self.__palindromo.setPalabra('Alejo')
        self.assertEqual(self.__palindromo.esPalindromo(), True)


if __name__ == '__main__':
    unittest.main()