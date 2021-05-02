import json
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_1228524.json"
data = urllib.request.urlopen(url).read()

info = json.loads(data)

numbers = 0

for num in range(len(info['comments'])):
   numbers = numbers + int(info['comments'][num]['count'])

print("Sum:", numbers)