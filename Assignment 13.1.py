import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_1228523.xml"
html = urllib.request.urlopen(url).read()

tree = ET.fromstring(html)
count = tree.findall('.//comment')
print("Count", len(count))

numbers = 0

for num in count: 
    nmb = int(num.find("count").text)
    numbers = numbers + nmb

print("Sum:", numbers)
