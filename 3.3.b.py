# ask user for two ditinct integer numbers
num1 = int(input("inter first integer number: "))
num2 = int(input("inter second integer number: "))
# display numbers user inputed 
print(f'integer one:{num1}')
print(f'integer two:{num2}')
# and operator
if num1 % 2 == 0 and num2 % 2 == 0:
    print("both numbers even: TRUE ")
else:
     print("both numbers even: FALSE")
if num1 < 50 and num2 < 50:
     print("both numbers less than 50: TRUE")
else:
     print("both numbers less than 50: FALSE ")
# or operater
if num1 % 7 == 0 or num2 % 7 == 0:
     print("one of the numbers is divisible by 7: TRUE")
else:
     print("one of the numbers is divisible by 7: FALSE")
if num1 * 2 > 100 or num2 * 2 > 100:
     print("one of numbers times 2 is greater than 100: TRUE")
else:
     print("one of numbers times 2 is greater than 100: FALSE")
# not operater
if not num1 > num2:
     print("number 1 is greater than number 2: FALSE")
else:
     print("number 1 is greater than number 2: TRUE")
if not num1 + num2 > 100:
     print(" number 1 plus number 2 is greater than 100: FALSE") 
else: 
     print("number 1 plus number 2 is greater than 100: TRUE")
    
