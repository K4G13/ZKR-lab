from PIL import Image
import sys

def toBin(n):
    b = "{0:b}".format(int(n))
    while len(b) < 8:
        b = '0' + b
    return b

def toDec(str):
    n = 0
    for i in range(len(str)):
        if str[len(str)-i-1] == '1':
            n += 2**i
    return n

def placeMsgInImg(msg):
    secret_msg = msg
    secret_msg_b = ""
    for i in secret_msg:
        secret_msg_b += toBin(ord(i))

    iterator = 0

    for h in range(height):
        for w in range(width):

            pxls = img.getpixel((w,h))
            new_pxls = []

            # print(f"{h*height+w}.\t",end="")

            for x in pxls:

                if iterator>=len(secret_msg_b): 
                    new_pxls.append(toDec( toBin(x)[:-1]+'1' ))
                    continue  

                if secret_msg_b[iterator] == '0':
                    new_pxls.append(toDec( toBin(x)[:-1]+'0' ))
                else:
                    new_pxls.append(toDec( toBin(x)[:-1]+'1' ))

                iterator+=1        
            
            # print(list(map(toBin,new_pxls)))
            img.putpixel((w,h),tuple(new_pxls))

    img.save("image.png")
    # print(secret_msg_b)

def readMsgFromImg():
    msg = ""
    buf = ""
    for h in range(height):
        for w in range(width):

            pxls = img.getpixel((w,h))

            for x in pxls:
                buf = buf + toBin(x)[-1]
                if len(buf) == 8: 
                    if buf == "11111111": 
                        print(msg)
                        return
                    # print(buf,end="\t")
                    msg = msg + chr(toDec(buf))
                    # print(chr(toDec(buf)))
                    buf = ""
    print(msg)
  
img = Image.open(r"image.png")
height = img.size[0]
width = img.size[1]

if len(sys.argv) >= 2:
    msg = ""
    for el in sys.argv[1:]:
        msg += el + " "
    placeMsgInImg(msg)
else:
    readMsgFromImg()