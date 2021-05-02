hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
try:
    hoursf = float(hrs)
    ratef = float(rate)
except:
    print("Not a number")
    quit()

pay = 0 
if hoursf < 40:
    pay = hoursf * ratef
    print(pay)
else:
    abovehours = hoursf - 40
    hrpay = abovehours * ratef * 1.5
    pay = ((hoursf - abovehours) * ratef) + hrpay
    print(pay)
