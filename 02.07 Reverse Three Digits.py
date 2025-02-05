number = int(input("Enter a 3 Digit Number: "))
hundreds = number // 100 
tens = number // 10 
tens = tens % 10
ones = number % 10 
ones = ones * 100
tens = tens * 10
sum = hundreds + tens + ones
print("Reverse of Digits:",sum)


