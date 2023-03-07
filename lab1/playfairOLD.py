import re
dev = False

print("\n  \033[92mP L A Y F A I R   C I P H E R\033[0m")
print("  [1]: encode\n  [2]: decode\n")
mode = ""
while(True):
    mode = input("Type '1' or '2': ")
    if mode == '1' or mode == '2': break

alphabet = []
for i in range(26):
    if chr(ord('a')+i) == 'j': continue
    alphabet.append(chr(ord('a')+i).upper())

keyword = input("Type keyword: ")
keyword = keyword.replace('j','i')
keyword = re.sub(r'[^a-zA-Z]', '', keyword)
keyword = "".join(dict.fromkeys(keyword)).upper()
#print(f"Keyword: \033[92m{keyword}\033[0m")

letters = [i for i in keyword] + [i for i in alphabet if i not in keyword]
matrix = []
for i in range(5):
    matrix.append(letters[i*5:i*5+5])
if dev: print(f"\033[93m{matrix[0]}\n{matrix[1]}\n{matrix[2]}\n{matrix[3]}\n{matrix[4]}\033[0m")
        


def rowIndex(letter):
    for row in range(5):
        for i in range(5):
            if letter == matrix[row][i]: return row

def colIndex(letter):
    for col in range(5):
        for i in range(5):
            if letter == matrix[i][col]: return col



# ENCODE
if mode == '1': 
    plaintext = input("Type text to encode: ")
    if plaintext == "":
        exit("\033[91mNO TEXT TO ENCODE\nEXITING...\033[0m")
    plaintext = plaintext.replace('j','I')
    plaintext = plaintext.replace('J','I')
    plaintext = re.sub(r'[^a-zA-Z]', '', plaintext).upper()
    
    print("")
    print(f"KEYWORD:   \033[92m{keyword}\033[0m")
    print(f"PLAINTEXT: \033[92m{plaintext}\033[0m (no spaces & j=i)")

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
        plaintext += 'X'

    if dev: print(f"DIAGRAM: \033[93m{plaintext[0]}{plaintext[1]}\033[0m",end="")
    for i in range(3,len(plaintext),2): 
        if dev: print(f"-\033[93m{plaintext[i-1]}{plaintext[i]}\033[0m",end="")
    if dev: print("")

    cipher = ""
    for i in range(0,len(plaintext),2):
        if rowIndex(plaintext[i]) == rowIndex(plaintext[i+1]):

            if colIndex(plaintext[i]) != 4:
                cipher+=matrix[rowIndex(plaintext[i])][colIndex(plaintext[i])+1]
            else:
                cipher+=matrix[rowIndex(plaintext[i])][0]

            if colIndex(plaintext[i+1]) != 4:
                cipher+=matrix[rowIndex(plaintext[i+1])][colIndex(plaintext[i+1])+1]
            else:
                cipher+=matrix[rowIndex(plaintext[i+1])][0]

        elif colIndex(plaintext[i]) == colIndex(plaintext[i+1]):
            
            if rowIndex(plaintext[i]) != 4:
                cipher+=matrix[rowIndex(plaintext[i])+1][colIndex(plaintext[i])]
            else:
                cipher+=matrix[rowIndex(plaintext[i])][0]

            if rowIndex(plaintext[i+1]) != 4:
                cipher+=matrix[rowIndex(plaintext[i+1])+1][colIndex(plaintext[i+1])]
            else:
                cipher+=matrix[rowIndex(plaintext[i+1])][0]

        else:
            cipher += matrix[rowIndex(plaintext[i])][colIndex(plaintext[i+1])]
            cipher += matrix[rowIndex(plaintext[i+1])][colIndex(plaintext[i])]

    if dev: print(f"CIPHER:  \033[93m{cipher[0]}{cipher[1]}\033[0m",end="")
    for i in range(3,len(cipher),2): 
        if dev: print(f"-\033[93m{cipher[i-1]}{cipher[i]}\033[0m",end="")
    if dev: print("")

    print(f"CIPHER:    \033[92m{cipher}\033[0m")   


# DECODE
elif mode == '2':
    cipher = input("Type text to decode: ")
    if cipher == "":
        exit("\033[91mNO TEXT TO DECODE\nEXITING...\033[0m")
    cipher = cipher.replace('j','I')
    cipher = cipher.replace('J','I')
    cipher = re.sub(r'[^a-zA-Z]', '', cipher).upper()

    print("")
    print(f"KEYWORD:   \033[92m{keyword}\033[0m")
    print(f"CIPHER:    \033[92m{cipher}\033[0m")

    plaintext = ""
    for i in range(0,len(cipher),2):
        if rowIndex(cipher[i]) == rowIndex(cipher[i+1]):

            if colIndex(cipher[i]) != 0:
                plaintext+=matrix[rowIndex(cipher[i])][colIndex(cipher[i])-1]
            else:
                plaintext+=matrix[rowIndex(cipher[i])][4]

            if colIndex(cipher[i+1]) != 0:
                plaintext+=matrix[rowIndex(cipher[i+1])][colIndex(cipher[i+1])-1]
            else:
                plaintext+=matrix[rowIndex(cipher[i+1])][4]

        elif colIndex(cipher[i]) == colIndex(cipher[i+1]):
            
            if rowIndex(cipher[i]) != 0:
                plaintext+=matrix[rowIndex(cipher[i])-1][colIndex(cipher[i])]
            else:
                plaintext+=matrix[rowIndex(cipher[i])][4]

            if rowIndex(cipher[i+1]) != 0:
                plaintext+=matrix[rowIndex(cipher[i+1])-1][colIndex(cipher[i+1])]
            else:
                plaintext+=matrix[rowIndex(cipher[i+1])][4]

        else:
            plaintext += matrix[rowIndex(cipher[i])][colIndex(cipher[i+1])]
            plaintext += matrix[rowIndex(cipher[i+1])][colIndex(cipher[i])]

    if dev: print(f"PLAINTEXT: \033[93m{plaintext[0]}{plaintext[1]}\033[0m",end="")
    for i in range(3,len(plaintext),2): 
        if dev: print(f"-\033[93m{plaintext[i-1]}{plaintext[i]}\033[0m",end="")
    if dev: print("")

    if plaintext[-1]=='X': plaintext = plaintext[:-1]

    print(f"PLAINTEXT: \033[92m{plaintext}\033[0m (no spaces & j=i)")   
    