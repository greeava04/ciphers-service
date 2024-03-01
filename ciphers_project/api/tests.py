from django.test import TestCase
from .ciphers import caesar_encode

# Create your tests here.
class CaesarCipherTest(TestCase):
    def test_caesar_cipher_1(self):
        plain_text = 'hello'
        shift=1
        expected_cipher_text = 'ifmmp'
        output=caesar_encode(plain_text,shift)
        self.assertEqual(output,expected_cipher_text)

    def test_caesar_cipher_2(self):
        plain_text = 'winter'
        shift=3
        expected_cipher_text = 'zlqwhu'
        output=caesar_encode(plain_text,shift)
        self.assertEqual(output,expected_cipher_text)
