fname = input("Enter file name:")
try:
    text = open(fname)
except:
    print("ERROR: could not find file called",fname)
    quit()

counts = dict()
for line in text:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("Word:", bigword,"Count:", bigcount)