text = "X-DSPAM-Confidence:    0.8475"
num_beginning = text.find(":")
number = text[num_beginning+1:]
print(float(number))

