import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Lauryn.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

cnt = input("Enter count: ")
pst = input("Enter position: ")

count = int(cnt)
position = int(pst)

for x in range(count):
    tags = soup('a')
    tag = tags[position-1]
    next_tag = tag.get('href', None)
    print(next_tag)

    url = str(next_tag)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

