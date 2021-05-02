text = open('mbox-short.txt')

address = list()
temp = list()
count = 0
for line in text:
    line = line.rstrip()
    if not line.startswith("From "): continue
    temp = line.split()
    address.append(temp[1])
    count = count + 1

separator = "\n"
print(separator.join(address))
print("There were", count, "lines in the file with From as the first word")
