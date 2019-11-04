hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs > 40:
    result = hrs * rate
    a = (hrs - 40) * (rate * 0.5)
    result = result + a
else:
    result = hrs * rate

print(result)