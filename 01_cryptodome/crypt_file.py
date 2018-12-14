from Crypto.PublicKey import RSA

class CryptFile(object):
    """ Encrypt and decrypt file
    """

    def __init__(self):
        pass

    def generate_RSA(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open("public.pem", "wb")
        file_out.write(public_key)

if __name__ == "__main__":
    crypt_file = CryptFile()
    crypt_file.generate_RSA()



    