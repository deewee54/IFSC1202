number = int(input("Enter a 3 Digit Number: "))
hundreds = number // 100
number = number % 100 
tens = number // 10
ones = number % 10
sum = hundreds + tens + ones 
print("Sum of Digits:",sum)
