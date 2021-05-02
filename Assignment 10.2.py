fname = input("Enter file name: ")
try:
    text = open(fname)
except:
    print("ERROR: could not find file called",fname)
    quit()

hours = list()
temp = list()

for line in text:
    line = line.rstrip()
    if not line.startswith("From "): continue
    temp = line.split()
    hours.append(temp[5][:2])

counts = dict()
for hrs in hours:
    counts[hrs] = counts.get(hrs,0) + 1

lst = list()
for key,value in counts.items():
    tmp = (key,value)
    lst.append(tmp)

lst.sort()
for key,value in lst:
    print(key,value)
