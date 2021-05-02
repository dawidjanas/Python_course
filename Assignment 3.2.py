hrs = input("Enter Hours: ")
hoursf = float(hrs)

rate = input("Enter rate: ")
ratef = float(rate)

pay = 0
if hoursf < 40:
    pay = hoursf * ratef
    print(pay)
else:
    abovehours = hoursf - 40
    hrpay = abovehours * ratef * 1.5
    pay = ((hoursf - abovehours) * ratef) + hrpay
    print(pay)
