def computepay(hours, rate):
    if hours < 40:
        pay = hours * rate
        return 
    else:
        above_hours = hours - 40
        above_rate = above_hours * rate * 1.5
        pay = ((hours - above_hours) * rate) + above_rate
        return pay

hrs = input("Enter Hours: ")
rte = input("Enter Rate: ")

try:
    work_hours = float(hrs)
    work_rate = float(rte)
except:
    print("ERROR: Not a number")
    quit()

salary = computepay(work_hours, work_rate)
print("Pay", salary)