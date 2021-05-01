from PIL import Image, ImageFont, ImageDraw
      
import textwrap

def getSmudgeMeme(text:str, lower_text:str) -> Image :
    stroke_color = (0, 0, 0)

    image = Image.open("assests\smudge_pic.png") 
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("LuckiestGuy.ttf", 120)

    # text = 'HI I'M SMUDGE'

    # lower_text = 'ENTER TEXT'

    W, H = image.size

    w, h = draw.textsize(text)
    
    # draw.text(((W-w)/2,(H-h)/2), text, font = font, align="center")
    
    # image.show()
    lines = textwrap.wrap(text, width=20)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((W - width) / 2, y_text), line, font=font, align="center", stroke_fill=stroke_color, stroke_width=5)
        y_text += height


    w1, h1 = draw.textsize(lower_text)

    l_lines = textwrap.wrap(lower_text, width=20)
    y_text = H - (h1*len(l_lines))*9
    for line in l_lines:
        width, height = font.getsize(line)
        draw.text(((W - width) / 2, y_text), line, font=font, align="center", stroke_fill=stroke_color, stroke_width=5)
        y_text += height
    # image.show()

    return image


if __name__ == "__main__":

    print("\n SMUDGE MEME CREATOR \n")
    upper_text = input("Enter upper text\n -> ")
    lower_text = input("Enter lower text\n -> ")


    if upper_text == '' or lower_text == '':
        upper_text = 'HI I\'M SMUDGE'
        lower_text = 'ENTER TEXT'
    img = getSmudgeMeme(upper_text,lower_text)
    img.save("exports/meme.png")
    import os
    os.system("exports\meme.png")
