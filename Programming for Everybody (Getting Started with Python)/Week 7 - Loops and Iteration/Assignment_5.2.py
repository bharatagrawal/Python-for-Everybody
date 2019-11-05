num= int(input("number:"))
largest = num
smallest = num
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid input");continue
    if largest<num:
        largest=num
    if smallest>num:
        smallest=num

print("Maximum is", largest)
print("Minimum is",smallest)