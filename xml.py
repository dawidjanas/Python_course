import xml.etree.ElementTree as ET

#XML text
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4421
    </phone>
    <email hide="yes"/>
</person>'''

#Wyświetlenie zawartości z XML
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))