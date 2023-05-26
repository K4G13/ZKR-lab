from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class ECB:
    def encode(msg,key):
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(msg, AES.block_size))
        return ciphertext
    def decode(msg_encoded,key):
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(msg_encoded), AES.block_size)
        return plaintext

class myCBC:
    def encode(key, iv, plaintext):
        ciphertext = b""
        previous_block = iv

        for i in range(0, len(plaintext), AES.block_size):
            block = plaintext[i:i + AES.block_size]

            block = bytes([a ^ b for a, b in zip(block, previous_block)])

            encrypted_block = ECB.encode(block,key)

            ciphertext += encrypted_block
            previous_block = encrypted_block

        return ciphertext
    
    def decode(key, iv, ciphertext):
        plaintext = b""
        previous_block = iv

        for i in range(0, len(ciphertext), AES.block_size):
            block = ciphertext[i:i + AES.block_size]

            decrypted_block = ECB.decode(block,key)

            decrypted_block = bytes([a ^ b for a, b in zip(decrypted_block, previous_block)])

            plaintext += decrypted_block
            previous_block = block

        return plaintext

KEY = get_random_bytes(16) 
IV = get_random_bytes(16) 
PLAINTEXT = b"Kryptografia!!!" 

ciphertext = myCBC.encode(KEY, IV, PLAINTEXT)
print("Szyfrogram:", ciphertext.hex())

decrypted_text = myCBC.decode(KEY, IV, ciphertext)
print("Tekst odszyfrowany:", decrypted_text.decode())