number1 = int(input("Enter First 2 Digit Number: "))
number2 = int(input("Enter Second 2 Digit Number: "))
number11 = number1 // 10
number12 = number1 % 10 
number21 = number2 // 10
number22 = number2 % 10 
number11 = number11 * 1000
number12 = number12 * 10 
number21 = number21 * 100
sum = number11 + number12 + number21 + number22
print("Merged Number:",sum)