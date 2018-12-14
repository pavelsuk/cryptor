from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

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
    
    def encrypt_data(self, data, fname):
        with open(fname, 'wb') as out_file:
            recipient_key = RSA.import_key(open('public.pem').read())
            session_key = get_random_bytes(16)
        
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)
        
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            [ out_file.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]

    def decrypt_data(self, fname, _passphrase = None):
        with open(fname, 'rb') as fobj:
            private_key = RSA.import_key(
                open('private.pem').read(),
                passphrase=_passphrase)
        
            enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                        for x in (private_key.size_in_bytes(), 
                                                        16, 16, -1) ]
        
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)
        
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            return data

if __name__ == "__main__":
    crypt_file = CryptFile()
    crypt_file.generate_RSA()



    