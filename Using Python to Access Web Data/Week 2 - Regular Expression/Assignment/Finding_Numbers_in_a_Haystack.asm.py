import re
sum = 0
file = open('regex_sum_300747.txt', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if len(numbers)>=1:
        for number in numbers:
            sum += int(number)

print(sum)
