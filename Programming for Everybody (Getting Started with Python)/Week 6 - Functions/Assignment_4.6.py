def computepay(hours,rate):
    if hours<40:
        pay =hours*rate
    else:
        overtime = hours-40
        pay = (40*rate)+(1.5*rate*overtime)
    
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("enter rate:"))
p = computepay(hrs,rate)
print(p)