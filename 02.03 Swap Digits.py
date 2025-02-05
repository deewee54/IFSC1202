number = int(input("Enter a number: "))
onestoTen = number % 10
onestoTen = onestoTen * 10
TenstoOnes = number // 10
number = onestoTen + TenstoOnes
print("Swapped Number:",number)