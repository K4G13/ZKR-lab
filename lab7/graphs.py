from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from timeit import default_timer as timer
import plotly.graph_objects as go

KEY = get_random_bytes(16) 
# MSG = b'hello message :)'

class ECB:
    def encode(msg,key):
        cipher = AES.new(key, AES.MODE_ECB)
        msg_encoded = cipher.encrypt(pad(msg,AES.block_size))
        return msg_encoded,0
    def decode(msg_encoded,key,nothing=0):
        decipher = AES.new(key, AES.MODE_ECB)
        msg_dec = decipher.decrypt(msg_encoded)
        msg = unpad(msg_dec, AES.block_size)
        return msg

class CBC:
    def encode(msg,key):
        cipher = AES.new(key, AES.MODE_CBC)
        cipher_text = cipher.encrypt(pad(msg, AES.block_size))
        iv = cipher.iv
        return cipher_text,iv
    def decode(msg_encoded,key,iv):
        decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = unpad( decrypt_cipher.decrypt(msg_encoded) ,AES.block_size)
        return plain_text

class CTR:
    def encode(msg,key):
        cipher = AES.new(key, AES.MODE_CTR)
        cipher_text = cipher.encrypt(msg)
        nonce = cipher.nonce
        return cipher_text,nonce
    def decode(msg_encoded,key,nonce):
        decrypt_cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        plain_text = decrypt_cipher.decrypt(msg_encoded)
        return plain_text

file1 = open("plik1.txt", "r").read()
file2 = open("plik2.txt", "r").read()
file3 = open("plik3.txt", "r").read()
files  = [file1,file2,file3]

def count_times(object):
    times_e = []
    times_d = []
    for file in files:
        start = timer()
        x,y = object.encode(file.encode(),KEY)
        end = timer()
        times_e.append(end-start)
        start = timer()
        object.decode(x,KEY,y)
        end = timer()
        times_d.append(end-start)
    return times_e,times_d

def show_grafs():

    file_sizes = [len(file1),len(file2),len(file3)]
    
    fig = go.Figure()
    enc_t,dec_t = count_times(ECB)
    fig.add_trace(go.Scatter(x=file_sizes, y=enc_t,
                        mode='lines+markers',
                        name='ECB'))
    enc_t,dec_t = count_times(CBC)
    fig.add_trace(go.Scatter(x=file_sizes, y=enc_t,
                        mode='lines+markers',
                        name='CBC'))
    enc_t,dec_t = count_times(CTR)
    fig.add_trace(go.Scatter(x=file_sizes, y=enc_t,
                        mode='lines+markers',
                        name='CTR'))
    fig.update_layout(title='encryption times',
                    xaxis_title='bytes',
                    yaxis_title='time [s]')
    fig.show()

    fig2 = go.Figure()
    enc_t,dec_t = count_times(ECB)
    fig2.add_trace(go.Scatter(x=file_sizes, y=dec_t,
                        mode='lines+markers',
                        name='ECB'))
    enc_t,dec_t = count_times(CBC)
    fig2.add_trace(go.Scatter(x=file_sizes, y=dec_t,
                        mode='lines+markers',
                        name='CBC'))
    enc_t,dec_t = count_times(CTR)
    fig2.add_trace(go.Scatter(x=file_sizes, y=dec_t,
                        mode='lines+markers',
                        name='CTR'))
    fig2.update_layout(title='decription times',
                    xaxis_title='bytes',
                    yaxis_title='time [s]')
    fig2.show()

show_grafs()