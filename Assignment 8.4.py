fname = input("Enter file name: ")
try: 
    text = open(fname)
except:
    print("ERROR: could not find file called",fname)
    quit()

words = []

for line in text:
    line = line.rstrip().split()
    for i in range(len(line)):
        if line[i] not in words:
            words.append(line[i])
    
sorted_words = sorted(words)
print(sorted_words)


