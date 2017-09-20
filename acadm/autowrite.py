from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
import argparse
import json
import os.path
import zipfile

try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO


def get_arguments():
    parser = argparse.ArgumentParser(
        description='A simple tool to credit your friend\'s assignment to yourself')

    parser.add_argument(
        'content',
        metavar='CONTENT',
        help='.dwg or converted image as an input')
    parser.add_argument(
        '-n',
        '--name',
        help='your name')
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


def dwg_to_jpg(filepath):
    with open(filepath, 'r') as filein:
        content = filein.read()

    filename = os.path.basename(filepath)

    url = 'https://coolutils.org/upload2.php'
    headers={'content-type': 'multipart/form-data; '
             'boundary=---------------------------1090027043118981933681270900'}
    data=(b'-----------------------------1090027043118981933681270900\r\n'
     b'Content-Disposition: form-data; name="files[]"; filename="{0}\r\n'
     b'Content-Type: text/plain\r\n\r\n'
     b'{1}\n\r\n'
     b'-----------------------------1090027043118981933681270900--\r\n').format(filename, content)

    response = requests.post(url, headers=headers, data=data)

    parsed = json.loads(response.text)
    result_name = parsed['files'][0]['name']

    url = 'https://coolutils.org/cad_convert.php'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data=b'Flag=1&srcfile={0}&src=0&fmt=jpg'.format(result_name)
    response = requests.post(url, headers=headers, data=data)

    zipped = zipfile.ZipFile(StringIO(response.content))

    raw_name = filename.split('.')[0]
    image_name = raw_name + '.Layout1.jpg'
    image_read = zipped.read(image_name)
    image_path = StringIO(image_read)

    return image_path


def command_line():
    args = get_arguments()
    content = args.content
    name = args.name
    uid = args.uid
    branch = args.branch
    sheet = args.sheet
    title1 = args.title1
    title2 = args.title2

    if content.endswith('.dwg'):
        print('converting ' + content + ' to jpg')
        content = dwg_to_jpg(content)

    print('making expected changes in the image')

    img = Image.open(content)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Times_New_Roman.ttf", 86)
    titlefont = ImageFont.truetype("Times_New_Roman.ttf", 99)

    # write name
    if name:
        draw.rectangle(((5004, 4668), (5858, 4874)), fill="white")
        draw.text((5005, 4740), name, (0,0,0), font=font)

    # write UID
    if uid:
        draw.rectangle(((5132, 4912), (5856, 5108)), fill="white")
        draw.text((5138, 4962), uid, (0,0,0), font=font)

    # write branch
    if branch:
        draw.rectangle(((5096, 5156), (5852, 5348)), fill="white")
        draw.text((5110, 5216), branch, (0,0,0), font=font)

    # write sheet no.
    if sheet:
        draw.rectangle(((6828, 5032), (7056, 5168)), fill="white")
        draw.text((6838, 5064), sheet, (0,0,0), font=font)

    # write title
    if title1:
        draw.rectangle(((5904, 4680), (7056, 4980)), fill="white")
        draw.text((5936, 4733), title1, (0,0,0), font=titlefont)
    if title2:
        draw.text((5938, 4839), title2, (0,0,0), font=titlefont)

    outfile = 'result.jpg'
    print('saving output to ' + outfile)
    img.save(outfile)


if __name__ == '__main__':

    command_line()
