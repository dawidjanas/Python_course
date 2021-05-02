fname = input("Enter the file name: ")
try:
    text = open(fname)
except:
    print("ERROR: could not find file called", fname)
    quit()

for line in text:
    print(line.upper().rstrip())