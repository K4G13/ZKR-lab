from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
BLOCK_SIZE = 32 # Bytes

key = 'abcdefghijklmnop'
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
msg = cipher.encrypt(pad(b'hello', BLOCK_SIZE))
print(msg.hex())

decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
msg_dec = decipher.decrypt(msg)
print(unpad(msg_dec, BLOCK_SIZE))