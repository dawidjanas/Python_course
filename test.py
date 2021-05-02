import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 4
position = 3

tags_lst = []

for x in range(count):

    tags = soup('a')

    my_tags = tags[position-1]

    needed_tag = my_tags.get('href', None)

    tags_lst.append(needed_tag)

    url = str(needed_tag)

    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')
print(tags_lst)