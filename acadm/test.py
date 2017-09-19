from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("test.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Times_New_Roman.ttf", 86)

# write name
draw.rectangle(((5002, 4668), (5858, 4874)), fill="white")
draw.text((5005, 4740),"RITIEK MALHOTRA",(0,0,0),font=font)

# write UID
draw.text((5138, 4962),"17BCS1752",(0,0,0),font=font)


img.save('sample-out.jpg')
