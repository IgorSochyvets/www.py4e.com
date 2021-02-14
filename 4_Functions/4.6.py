def computepay(hours,rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rateInt) + ( (hoursInt - 40) * rateInt * 1.5 )
    return(pay)


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try: 
    hoursInt = int(hours)
    rateInt = int(rate)
except:
    print("Error, please enter numeric input")
    exit()

salary = computepay(hoursInt,rateInt)
print("Pay: ",salary)
