numbers = [9,41,12,3,74,13]
smallest = numbers[0]
for the_num in numbers:
	if the_num < smallest:
		smallest = the_num
print("The smallest number is:", smallest)