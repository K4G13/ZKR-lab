import re
dev = True



print("\n  \033[92mPlayfair encoder/decoder\033[0m\n")
print("Choose mode:\n  [1]: encode\n  [2]: decode\n")
mode = ""
while(True):
    mode = input()
    if mode == '1' or mode == '2': break
    print("Type '1' or '2': ",end="")

alphabet = []
for i in range(26):
    if chr(ord('a')+i) == 'j': continue
    alphabet.append(chr(ord('a')+i).upper())

keyword = input("\nType keyword: ")
keyword = keyword.replace('j','i')
keyword = re.sub(r'[^a-zA-Z]', '', keyword)
keyword = "".join(dict.fromkeys(keyword)).upper()
print(f"Keyword: \033[92m{keyword}\033[0m")

letters = [i for i in keyword] + [i for i in alphabet if i not in keyword]
matrix = []
for i in range(5):
    matrix.append(letters[i*5:i*5+5])
if dev: print(f"\033[92m{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}\n{matrix[4]}\033[0m")
        


# ENCODE
if mode == '1': 
    plaintext = input("\nType text to encode: ")
    if plaintext == "":
        exit("\033[91mNO TEXT TO ENCODE\nEXITING...\033[0m")
    plaintext = plaintext.replace('j','i')
    plaintext = re.sub(r'[^a-zA-Z]', '', plaintext).upper()
    print(f"PLAINTEXT: \033[92m{plaintext}\033[0m (without spaces and j=i)")

    i=0
    while True:
        if len(plaintext)<=i: break
        if i%2 and plaintext[i]==plaintext[i-1]:
            if dev: print(f"\033[91m{plaintext[i]}\033[0m")
            plaintext = plaintext[:i] + "X" + plaintext[i:]
            if dev: print(f"\033[93m{plaintext[:i+1]}\033[0m",end="")
        else:
            if dev: print(f"\033[93m{plaintext[i]}\033[0m",end="")
        i+=1
    if dev: print("")
    if len(plaintext)%2 == 1:
        if plaintext[-1]!='X':
            plaintext += 'X'
        else:
            plaintext += 'Q'

    if dev: print(f"DIAGRAM: \033[92m{plaintext[0]}{plaintext[1]}\033[0m",end="")
    for i in range(3,len(plaintext),2): 
        if dev: print(f"-\033[92m{plaintext[i-1]}{plaintext[i]}\033[0m",end="")
    


# DECODE
elif mode == '2':
    plaintext = input("\nType text to decode: ")
    if plaintext == "":
        exit("\033[91mNO TEXT TO DECODE\nEXITING...\033[0m")
    plaintext = plaintext.replace('j','i')
    plaintext = re.sub(r'[^a-zA-Z]', '', plaintext).upper()
    print(f"PLAINTEXT: \033[92m{plaintext}\033[0m (without spaces and j=i)")