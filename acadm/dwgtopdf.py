import requests


random_code = 'A2B3cDEf'
output_file = 'AbCd123e'



with open('Ex2_Fig1.dwg', 'rb') as filein:
    content = filein.read()

url = 'http://www.pdfaid.com/Upload.ashx'

headers = {
         'Accept': '*/*',
         'Accept-Encoding': 'gzip, '
                            'deflate',
         'Accept-Language': 'en-US,en;q=0.5',
         'Connection': 'keep-alive',
         'Content-Type': 'multipart/form-data; '
                         'boundary=---------------------------3096710385416081101761760526',
         'Cookie': '_ga=GA1.2.438348521.1505234174; '
                   '_gid=GA1.2.1093387795.1505234174',
         'Referer': 'http://www.pdfaid.com/dwg-to-pdf-conversion.aspx',
         'User-Agent': 'Mozilla/5.0 '
                       '(X11; '
                       'Ubuntu; '
                       'Linux '
                       'x86_64; '
                       'rv:55.0) '
                       'Gecko/20100101 '
                       'Firefox/55.0'
    }

response = requests.post(url, headers=headers,
    data=(b'-----------------------------3096710385416081101761760526\r\nContent-Dispo'
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
)

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
    'InputFileName': random_code + '.dwg',
    'Keywords': '',
    'OutputFileName': output_file,
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

print('http://www.pdfaid.com/DownloadFiles/dwg2pdf_' + output_file + '.pdf')
