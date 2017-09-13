import requests


random_code = 'A2B3cDGf'
output_file = 'AbCd125e'


with open('Ex2_Fig1.dwg', 'rb') as filein:
    content = filein.read()

url = 'http://www.pdfaid.com/Upload.ashx'

headers = {
         'Content-Type': 'multipart/form-data; '
                         'boundary=---------------------------3096710385416081101761760526',
    }

data = (b'-----------------------------3096710385416081101761760526\r\nContent-Dispo'
     b'sition: form-data; name="name"\r\n\r\nlinks.dwg\r\n-----------------------'
     b'------3096710385416081101761760526\r\nContent-Disposition: form-data; name'
     b'="chunk"\r\n\r\n0\r\n-----------------------------309671038541608110176176'
     b'0526\r\nContent-Disposition: form-data; name="chunks"\r\n\r\n1\r\n----------'
     b'-------------------3096710385416081101761760526\r\nContent-Disposition: fo'
     b'rm-data; name="Random"\r\n\r\n{0}\r\n-----------------------------309'
     b'6710385416081101761760526\r\nContent-Disposition: form-data; name="file"; '
     b'filename="links.dwg"\r\nContent-Type: application/vnd.VAR_VENDOR_NAME.VAR_'
     b'PRODUCT_NAME-dwg\r\n\r\n{1}'
     b'\n\r\n-----------------------------3096710385416081101761760526--\r'
     b'\n').format(random_code, content)

response = requests.post(url, headers=headers, data=data)
print(response.text)


url = 'http://www.pdfaid.com/dwg-to-pdf-conversion.aspx/ConvertFile'

json = {
    'Author': '',
    'Color': 'True Colors',
    'InputFileName': random_code + '.dwg',
    'Keywords': '',
    'OutputFileName': output_file,
    'Quality': 'Medium',
    'Subject': '',
    'Title': '',
}

response = requests.post(url=url, json=json)
print(response.text)

print('http://www.pdfaid.com/DownloadFiles/dwg2pdf_' + output_file + '.pdf')
