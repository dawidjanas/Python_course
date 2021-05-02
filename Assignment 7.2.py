fname = input("Enter the file name: ")
try:
    text = open(fname)
except:
    print("ERROR: couldn't open the file called", fname)
    quit()

count = 0
words = 0

for line in text:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        num = line.find(':')
        number = line[num+1:]
        words = words+ float(number)

average = words / count
print("Average spam confidence:", average)
