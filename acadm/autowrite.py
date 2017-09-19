from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description='A simple tool to credit your friend\'s assignment to yourself')

    parser.add_argument(
        'content',
        metavar='CONTENT',
        help='.dwg, or converted to .pdf or image as an input')
    parser.add_argument(
        '-n',
        '--name',
        help='your name',
        default='')
    parser.add_argument(
        '-u',
        '--uid',
        help='your UID')
    parser.add_argument(
        '-b',
        '--branch',
        help='your branch')
    parser.add_argument(
        '-s',
        '--sheet',
        help='sheet number')
    parser.add_argument(
        '-t1',
        '--title1',
        help='1st line of title')
    parser.add_argument(
        '-t2',
        '--title2',
        help='2nd line of title')

    return parser.parse_args()


def command_line():
    args = get_arguments()
    content = args.content
    name = args.name
    uid = args.uid
    branch = args.branch
    sheet = args.sheet
    title1 = args.title1
    title2 = args.title2

    img = Image.open(content)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Times_New_Roman.ttf", 86)
    titlefont = ImageFont.truetype("Times_New_Roman.ttf", 99)

    # write name
    draw.rectangle(((5004, 4668), (5858, 4874)), fill="white")
    draw.text((5005, 4740), name, (0,0,0), font=font)

    # write UID
    draw.rectangle(((5132, 4912), (5856, 5108)), fill="white")
    draw.text((5138, 4962), uid, (0,0,0), font=font)

    # write branch
    draw.rectangle(((5096, 5156), (5852, 5348)), fill="white")
    draw.text((5110, 5216), branch, (0,0,0), font=font)

    # write sheet no.
    draw.rectangle(((6828, 5032), (7056, 5168)), fill="white")
    draw.text((6838, 5064), sheet, (0,0,0), font=font)

    # write title
    draw.rectangle(((5904, 4680), (7056, 4980)), fill="white")
    draw.text((5936, 4733), title1, (0,0,0), font=titlefont)
    draw.text((5938, 4839), title2, (0,0,0), font=titlefont)


    img.save('result.jpg')


if __name__ == '__main__':

    command_line()
