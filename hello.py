import re

fname = ('mbox.txt')
text = open(fname)

domains = list()
for line in text:
  line = line.rstrip()
  piece = re.findall('^From \S+@(\S+)', line)
  if len(piece) == 0: continue
  for x in range(len(piece)):
    domains.append(piece[x])
print(domains)

