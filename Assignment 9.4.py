fname = input("Enter file name:")
try:
    text = open(fname)
except:
    print("ERROR: could not find file called",fname)
    quit()

address = list()
temp = list()

for line in text:
    if not line.startswith("From "): continue
    temp = line.split()
    address.append(temp[1])

counts = dict()
for words in address:
    counts[words] = counts.get(words,0) + 1

bigcount = None
bigwords = None

for keys, values in counts.items():
    if bigcount is None or values > bigcount:
        bigwords = keys
        bigcount = values

print(bigwords,bigcount)