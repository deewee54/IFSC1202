boys  = []
girls = [] 
file = open("Exam Two Names.txt", 'r')
for line in file: 
    boy, girl = line.strip().split(',')
    boys.append(boy.strip())
    girls.append(girl.strip())
file.close()

while True: 
    user_input = input("Enter a name: ").strip().capitalize()
    if user_input.lower() == 'q':
        break

    found = False 
    for i in range(len(boys)):
        if boys [i] == user_input: 
            print(f"Boy's Name - Rank: {i+1}")
            found = True 
            break 
        if girls[i] == user_input: 
            print(f"Girl's Name - Rank: {i + 1}")
            found = True 
            break
    if not found: 
        print("Name Not Found")