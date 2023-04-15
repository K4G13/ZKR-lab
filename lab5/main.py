from PIL import Image, ImageDraw, ImageFont
import random

WHITE = (255,255,255)
BLACK = (0,0,0)

def addPixels(px1,px2):
    r = 0
    g = 0  
    b = 0
    a = 0
    if px1[0] != 0 and px2[0] != 0:
        r = 255
    if px1[1] != 0 and px2[1] != 0:
        g = 255
    if px1[2] != 0 and px2[2] != 0:
        b = 255
    if px1[3] != 0 and px2[3] != 0:
        a = 255    
    return (r,g,b,a)

def drawText( image, text="text", position=(0,0), color=(255,0,0), bgColor=(0,0,0) ):

    position = (position[0]+1,position[1]+1)
    text = " "+text+" "

    draw = ImageDraw.Draw(image)
    bbox = draw.textbbox(position, text)
    draw.rectangle(bbox, fill = bgColor)
    draw.text(position, text, fill = color)

secretImg = Image.open(r"secret.png")
width = secretImg.size[0]
height = secretImg.size[1]

share1Img = Image.new( mode = "RGBA", size = (width, height) )
share2Img = Image.new( mode = "RGBA", size = (width, height) )

for y in range(height):
    for x in range(width):
        if secretImg.getpixel((x,y))[:3] == WHITE:
            if random.randint(0,1) == 0:
                share1Img.putpixel((x,y), WHITE )
                share2Img.putpixel((x,y), WHITE )
            else:
                share1Img.putpixel((x,y), BLACK )
                share2Img.putpixel((x,y), BLACK )
        else:
            if random.randint(0,1) == 0:
                share1Img.putpixel((x,y), WHITE )
                share2Img.putpixel((x,y), BLACK )
            else:
                share1Img.putpixel((x,y), BLACK )
                share2Img.putpixel((x,y), WHITE )

secretDecryptedImg = Image.new( mode = "RGBA", size = (width, height) )
for y in range(height):
    for x in range(width):
        secretDecryptedImg.putpixel((x,y), addPixels(share1Img.getpixel((x,y)),share2Img.getpixel((x,y))) )

summaryImg = Image.new( mode = "RGBA", size = (width*2, height*2), color = (255,255,255,255) )
for y in range(height):
    for x in range(width):
        summaryImg.putpixel((x, y), secretImg.getpixel((x,y)) )        
        summaryImg.putpixel((x, y+height), share1Img.getpixel((x,y)) )
        summaryImg.putpixel((x+width, y+height), share2Img.getpixel((x,y)) )
        summaryImg.putpixel((x+width, y), secretDecryptedImg.getpixel((x,y)) )

drawText(summaryImg,"secret",(0,0))
drawText(summaryImg,"decoded",(width,0))
drawText(summaryImg,"share1",(0,height))
drawText(summaryImg,"share2",(width,height))

share1Img.save("share_1.png")
share2Img.save("share_2.png")
secretDecryptedImg.save("secret_decrypted.png")
summaryImg.save("summary.png")