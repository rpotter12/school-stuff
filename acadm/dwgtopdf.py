import requests


url = 'http://www.pdfaid.com/Upload.ashx'

headers = {
        'Host': 'www.pdfaid.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.pdfaid.com/dwg-to-pdf-conversion.aspx',
        'Content-Length': '41100',
        'Content-Type': 'multipart/form-data; boundary=---------------------------20536363942023438477859369942',
        'Cookie': '_ga=GA1.2.438348521.1505234174; _gid=GA1.2.1093387795.1505234174; _gat=1',
        'Connection': 'keep-alive',
    }

with open('Ex2_Fig1.dwg', 'rb') as filein:
    content = filein.read()

data = {
        'name': 'Ex2_Fig1.dwg',
        'chunk': '0',
        'chunks': '1',
        'Random': 'SILVJOkU',
        'file': content
    }

response = requests.post(url, headers=headers, data=data)
print(response.text)


url = 'http://www.pdfaid.com/dwg-to-pdf-conversion.aspx/ConvertFile'

headers = {
    'Host': 'www.pdfaid.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json; charset=utf-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.pdfaid.com/dwg-to-pdf-conversion.aspx',
    'Content-Length': '151',
    'Cookie': '_ga=GA1.2.438348521.1505234174; _gid=GA1.2.1093387795.1505234174; _gat=1',
    'Connection': 'keep-alive',
}


json = {
    'Author': '',
    'Color': 'True Colors',
    'InputFileName': 'OT2TN3V9.dwg',
    'Keywords': '',
    'OutputFileName': 'z0xs3Df9',
    'Quality': 'Medium',
    'Subject': '',
    'Title': '',
}


response = requests.request(
    method='POST',
    url=url,
    headers=headers,
    json=json,
)

print(response.text)

print('http://www.pdfaid.com/DownloadFiles/dwg2pdf_z0xs3Df9.pdf')

'''import requests


with open('Ex2_Fig1.dwg', 'rb') as filein:
    content = filein.read()

data = {
        'name': 'Ex2_Fig1.dwg',
        'chunk': '0',
        'chunks': '1',
        'Random': 'OT2TN1V1',
        'file': content
    }

response = requests.post('http://www.pdfaid.com/Upload.ashx', data=data)
print(response.text)

data = {
    "Author": "",
    "Color": "True Colors",
    "InputFileName": "OT2TN1V1.dwg",
    "Keywords": "",
    "OutputFileName": "z0xs0Dfk",
    "Quality": "Medium",
    "Subject": "",
    "Title": ""
}

response = requests.post('http://www.pdfaid.com/dwg-to-pdf-conversion.aspx/ConvertFile', data=data)
print(response.text)

print('http://www.pdfaid.com/DownloadFiles/dwg2pdf_z0xs0Dflk.pdf')
'''
