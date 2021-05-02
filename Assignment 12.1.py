import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ("http://py4e-data.dr-chuck.net/comments_1228521.html")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
numbers = 0
for tag in tags:
    numbers = numbers + int(tag.contents[0])

print(numbers)