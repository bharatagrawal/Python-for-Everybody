score = float(input("Enter Score: "))

if score>=0.0 or score<=1.0:
    if(score>=0.9):
        grade = 'A'
        
    elif score>=0.8:
        grade = 'B'
        
    elif score>=0.7:
        grade = 'C'
        
    elif score>=0.6:
        grade = 'D'
     
    else:
        grade ='F'
    print(grade)
else:
    print("your input is incorrect. put the value between o.o to 1.0")
    