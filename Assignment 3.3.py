sc = input("Enter Score: ")
try:
    score = float(sc)
except:
    print("Not a number")
    quit()

if score > 1.0:
    print("Error - number out of range")
    quit()
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")