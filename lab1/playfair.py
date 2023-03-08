import sys
import re
dev = False

class logColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 4: 
    print(f"{logColors.FAIL}(!) Too few arguments")
    print(f"{logColors.FAIL}Correct usage: {logColors.WARNING}playfair.py [dev-][e|d|encode|decode] <keyword> <text>)")
    print(f"{logColors.FAIL}Example1: {logColors.WARNING}playfair.py e szyfr politechnika poznanska")
    print(f"{logColors.FAIL}Example2: {logColors.WARNING}playfair.py d szyfr QPGKXABIOHGDQPBUBMFGET")
    sys.exit(f"{logColors.FAIL}EXITING...{logColors.ENDC}")

mode = sys.argv[1]
if mode[0:4] == "dev-":
    dev = True
    mode = mode[4:]
if mode != "e" and mode != "d" and mode != "encode" and mode != "decode":
    sys.exit(f"{logColors.FAIL}(!) Wrong mode\nAvailable modes: {logColors.WARNING} e, d, encode, decode\n{logColors.FAIL}EXITING...{logColors.ENDC}")
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

    if dev: print(f"{logColors.WARNING}KEYWORD: {keyword}{logColors.ENDC}")
    if dev: print(f"{logColors.WARNING}{newMatrix[0]}\n{newMatrix[1]}\n{newMatrix[2]}\n{newMatrix[3]}\n{newMatrix[4]}{logColors.ENDC}")

    return newMatrix

def getRow(matrix,letter):
    for row in range(5):
        for i in range(5):
            if letter == matrix[row][i]: return row

def getCol(matrix,letter):
    for col in range(5):
        for i in range(5):
            if letter == matrix[i][col]: return col

def encode(M,T):
    T = T.replace('j','I')
    T = T.replace('J','I')
    T = re.sub(r'[^a-zA-Z]', '', T).upper()
    if dev: print(f"{logColors.WARNING}PLAINTEXT: {T} (no spaces & j=i){logColors.ENDC}")

    diagrams = ""
    for x in T:
        if diagrams!="" and len(diagrams)%2==1 and x==diagrams[-1]:
            diagrams += "X"
        diagrams += x
    if len(diagrams)%2 == 1:
        diagrams += 'X'
    if dev: 
        print(f"{logColors.WARNING}DIAGRAMS:  {diagrams[0]}{diagrams[1]}{logColors.ENDC}",end="")
        for i in range(2,len(diagrams),2):
            print(f"-{logColors.WARNING}{diagrams[i]}{diagrams[i+1]}{logColors.ENDC}",end="")
        print("")

    cipher = ""
    for i in range(0,len(diagrams),2):
        l1 = diagrams[i]
        l2 = diagrams[i+1]
        if getRow(M,l1) == getRow(M,l2):
            if getCol(M,l1) == 4:
                cipher += M[getRow(M,l1)][0]
            else:
                cipher += M[getRow(M,l1)][getCol(M,l1)+1]
            if getCol(M,l2) == 4:
                cipher += M[getRow(M,l2)][0]
            else:
                cipher += M[getRow(M,l2)][getCol(M,l2)+1]
        elif getCol(M,l1) == getCol(M,l2):
            if getRow(M,l1) == 4:
                cipher += M[0][getRow(M,l1)]
            else:
                cipher += M[getRow(M,l1)+1][getCol(M,l1)]
            if getRow(M,l2) == 4:
                cipher += M[0][getRow(M,l2)]
            else:
                cipher += M[getRow(M,l2)+1][getCol(M,l2)]
        else:
            cipher += M[getRow(M,l1)][getCol(M,l2)]
            cipher += M[getRow(M,l2)][getCol(M,l1)]
    
    if dev: 
        print(f"{logColors.WARNING}CIPHER:    {cipher[0]}{cipher[1]}{logColors.ENDC}",end="")
        for i in range(2,len(cipher),2):
            print(f"-{logColors.WARNING}{cipher[i]}{cipher[i+1]}{logColors.ENDC}",end="")
        print("")

    print(cipher)

def decode(M,T):
    T = T.replace('j','I')
    T = T.replace('J','I')
    T = re.sub(r'[^a-zA-Z]', '', T).upper()
    if len(T)%2==1:
        sys.exit(f"{logColors.FAIL}(!) Length of encoded text should be even number\nEXITING...{logColors.ENDC}")
    if dev: print(f"{logColors.WARNING}CIPHER: {T} (J=I){logColors.ENDC}")

    decodedText = ""
    for i in range(0,len(T),2):
        l1 = T[i]
        l2 = T[i+1]
        if l1 == l2:
            sys.exit(f"{logColors.FAIL}(!) Letters cannot repeat on 'n' and 'n+1' indexes\nEXITING...{logColors.ENDC}")
        if getRow(M,l1) == getRow(M,l2):
            if getCol(M,l1) == 0:
                decodedText += M[getRow(M,l1)][4]
            else:
                decodedText += M[getRow(M,l1)][getCol(M,l1)-1]
            if getCol(M,l2) == 0:
                decodedText += M[getRow(M,l2)][4]
            else:
                decodedText += M[getRow(M,l2)][getCol(M,l2)-1]
        elif getCol(M,l1) == getCol(M,l2):
            if getRow(M,l1) == 0:
                decodedText += M[4][getRow(M,l1)]
            else:
                decodedText += M[getRow(M,l1)-1][getCol(M,l1)]
            if getRow(M,l2) == 0:
                decodedText += M[4][getRow(M,l2)]
            else:
                decodedText += M[getRow(M,l2)-1][getCol(M,l2)]
        else:
            decodedText += M[getRow(M,l1)][getCol(M,l2)]
            decodedText += M[getRow(M,l2)][getCol(M,l1)]
    
    decodedText = decodedText.replace('X','')
    
    print(decodedText)



#MAIN
letterMatrix = createMatrix(keyword)
if mode == "e" or mode == "encode":
    encode(letterMatrix,text)
if mode == "d" or mode == "decode":
    decode(letterMatrix,text)