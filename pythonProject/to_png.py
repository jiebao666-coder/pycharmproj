import urllib
import sys
import urllib.parse
import ssl
import urllib.request


host = r'https://pdftoimage.market.alicloudapi.com'
path = r'/s/api/ocr/pdfToImage'
method = 'POST'
appcode = '71907e1500c74dd6ba9c5710530fd3ed'
querys = ''
bodys = {}
url = host + path

bodys['imgUrl'] = r"D:/pic/2020-2022henan.pdf"
bodys['pageNum'] = '''0'''
bodys['dpi'] = '''200'''
bodys['convertType'] = '''pdfbox'''
post_data = urllib.parse.urlencode(bodys).encode('utf-8')
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)

request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx).read().decode('utf-8')
content = response.read()
if content:
    print(content)