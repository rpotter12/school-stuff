from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("test.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Times_New_Roman.ttf", 86)

# write name
draw.rectangle(((5004, 4668), (5858, 4874)), fill="white")
draw.text((5005, 4740),"RITIEK MALHOTRA",(0,0,0),font=font)

# write UID
draw.rectangle(((5132, 4912), (5856, 5108)), fill="white")
draw.text((5138, 4962),"17BCS1752",(0,0,0),font=font)

# write branch
draw.rectangle(((5096, 5156), (5852, 5348)), fill="white")
draw.text((5110, 5216),"B.E. CSE",(0,0,0),font=font)

# write title
draw.rectangle(((5904, 4680), (7056, 4980)), fill="white")


img.save('sample-out.jpg')
