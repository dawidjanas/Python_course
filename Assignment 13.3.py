import json
import urllib.request, urllib.parse, urllib.error
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    location = dict()
    location['address'] = address
    if api_key is not False: location['key'] = api_key
    url = service_url + urllib.parse.urlencode(location)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != "OK":
        print("ERROR")
        continue

    result = js['results'][0]['place_id']
    print(result)

    