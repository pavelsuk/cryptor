import unittest
import logging


from crypt_file import CryptFile


class Test_CryptFile(unittest.TestCase):
    def setUp(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        # logger = logging.getLogger()
        # logger.addHandler(stream_handler)
        # logger.setLevel(logging.INFO)
        # self.logger.format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[stream_handler], force=True)

        logger = logging.getLogger()
        logger.debug("setUp test")

        self.crypt_file = CryptFile(logger)
        self._test_secret = 'this is my little secret'

    @unittest.skip("just temporary")
    def test_generate_key(self):
        self.crypt_file.generate_key()
        self.crypt_file.generate_key(
            private_key_fname='private_test.pem',
            public_key_fname='public_test.pem')

        self.crypt_file.generate_key(
            private_key_fname='private_test_pwd.pem',
            public_key_fname='public_test_pwd.pem',
            _passphrase='TestingPassphraseGoesHere')

    def test_encrypt_file(self):
        self.crypt_file.encrypt_file('little_secret.txt')
        self.crypt_file.encrypt_file('little_secret_null')
        self.crypt_file.encrypt_file('little_secret.txt',
                                     'encrypted_secret_default.enc')
        self.crypt_file.encrypt_file(
            'little_secret.txt',
            'encrypted_secret_test.enc',
            public_key_fname='public_test.pem')
        self.crypt_file.encrypt_file(
            'little_secret.txt',
            'encrypted_secret_test_pwd.enc',
            public_key_fname='public_test_pwd.pem')

    def test_encrypt_data(self):
        self.crypt_file.encrypt_data(
            self._test_secret.encode('utf-8'), 'data.encrypted')

    def test_decrypt_file(self):
        self.crypt_file.decrypt_file(
            'encrypted_secret_test.enc',
            'little_secret.txt.dec',
            private_key_fname='private_test.pem')
        with (self.assertRaises(ValueError)):
            self.crypt_file.decrypt_file(
                'encrypted_secret_test_pwd.enc',
                'little_secret_pwd.txt.dec',
                private_key_fname='private_test_pwd.pem')
        self.crypt_file.decrypt_file(
            'encrypted_secret_test_pwd.enc',
            'little_secret_pwd.txt.dec',
            private_key_fname='private_test_pwd.pem',
            _passphrase='TestingPassphraseGoesHere')

    def test_decrypt_data(self):
        data = self.crypt_file.decrypt_data('data.encrypted')
        self.assertEqual(data, self._test_secret.encode('utf-8'))

    def test_encrypt_dir(self):
        self.crypt_file.encrypt_dir('test_data\dir2encrypt', 'test_data\dir2decrypt', 'private*')

    def test_decrypt_dir(self):
        self.crypt_file.decrypt_dir('test_data\dir2decrypt', 'test_data\dir2encrypt', 'private*')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
