largest = None
smallest = None

while True:
    num = input("Enter a number, if you are done type done:")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print("Invalid input")

    if largest == None and smallest == None:
        largest = number
        smallest = number
    elif largest < number:
        largest = number
    elif smallest > number:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)