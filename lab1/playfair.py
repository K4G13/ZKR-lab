import sys
import re
dev = True

if len(sys.argv) < 4: 
    sys.exit("\033[91m(!) Too few arguments\nCorrect usage: \033[93mplayfair.py [e|d|encode|decode] <keyword> <text>\n\033[91mEXITING...\033[0m")

mode = sys.argv[1]
if mode != "e" and mode != "d" and mode != "encode" and mode != "decode":
    sys.exit("\033[91m(!) Wrong mode\nAvailable modes: \033[93m e\033[91m,\033[93m d\033[91m,\033[93m encode\033[91m,\033[93m decode\n\033[91mEXITING...\033[0m")
keyword = sys.argv[2]
text = ""
for i in range(3,len(sys.argv),1): text += sys.argv[i] + " "

def createMatrix(keyword):
    alphabet = []
    for i in range(26):
        if chr(ord('a')+i) == 'j': continue
        alphabet.append(chr(ord('a')+i).upper())

    keyword = keyword.replace('j','i')
    keyword = re.sub(r'[^a-zA-Z]', '', keyword)
    keyword = "".join(dict.fromkeys(keyword)).upper()

    letters = [i for i in keyword] + [i for i in alphabet if i not in keyword]
    newMatrix = []
    for i in range(5):
        newMatrix.append(letters[i*5:i*5+5])

    if dev: print(f"\033[93mKEYWORD: {keyword}\033[0m")
    if dev: print(f"\033[93m{newMatrix[0]}\n{newMatrix[1]}\n{newMatrix[2]}\n{newMatrix[3]}\n{newMatrix[4]}\033[0m")

    return newMatrix
matrix = createMatrix(keyword)