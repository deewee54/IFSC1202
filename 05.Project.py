start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special Numbers between {start} and {end}")

for num in range(start,end + 1):
    count = 0
    temp = num
    while temp > 0:
        temp //= 10
        count += 1
    sumofnumber = 0
    temp = num 
    while temp > 0: 
        digit = temp % 10
        sumofnumber += digit ** count 
        temp //= 10 
    if sumofnumber == num:
        print(num)
