import re
try:
    text = open("regex_sum_1228519.txt")
except:
    print("ERROR: could not find this file")
    quit()

count = 0
numbers = list()

for line in text:
    line = line.rstrip()
    nmb = re.findall('[0-9]+',line)
    if len(nmb) == 0: continue
    
    for x in range(len(nmb)):
        number = int(nmb[x])
        numbers.append(number)
        count = count + 1

print("Sum = ",sum(numbers))
print(count, "values")