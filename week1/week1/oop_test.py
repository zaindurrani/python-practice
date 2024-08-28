num1 = 4
num2 = 5
num3 = 6
#find the greatest number of these by if else

"""
    if num1 > num2 > num3:
    print("num1 is greatest")
if num1 < num2 > num3:
    print("num2 is greatest")
elif num1 < num2 < num3:
    print("num3 is greatest of all")
    
    """
score = int(input("input your score between 0 and 100: "))
while score < 0 or score > 100:
    input("enter the values between 0 and 100 only: ")
else: 
    print("your grades are ", score)