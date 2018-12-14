import unittest

from crypt_file import CryptFile


class Test_AsusRouter(unittest.TestCase):

    def setUp(self):
        self.crypt_file = CryptFile()
        self._test_secret = 'this is my little secret'

    
    def test_generate_RSA(self):
        # self.crypt_file.generate_RSA()
        pass

    def test_encrypt_data(self):
        self.crypt_file.encrypt_data(self._test_secret.encode('utf-8'),'little_secret.encrypted')

    def test_decrypt_data(self):
        data = self.crypt_file.decrypt_data('little_secret.encrypted')
        self.assertEqual(data, self._test_secret.encode('utf-8'))

    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main()   