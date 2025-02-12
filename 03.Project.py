
firstnumber = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
secondnumber = float(input("Enter Second Number: "))
if operator == '+':
    answer = firstnumber + secondnumber
    print(firstnumber,operator,secondnumber,"=",answer)
if operator == '-':
    answer = firstnumber - secondnumber
    print(firstnumber,operator,secondnumber,"=",answer)
if operator == '*':
    answer = firstnumber * secondnumber
    print(firstnumber,operator,secondnumber,"=",answer)
if operator == '/':
    answer = firstnumber / secondnumber
    print(firstnumber,operator,secondnumber,"=",answer)
else: 
    print("Invalid Operator")
