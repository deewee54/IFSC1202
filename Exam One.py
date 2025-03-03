from random import randint 
user = input(f"What is the Your Name? ")
userscore = 0
computerscore = 0
while userscore < 30 and computerscore < 30: 
    input("")
    userroll = randint(1,6)
    print(f"{user} rolled : {userroll}")
    computerroll = randint(1,6)
    print(f"Computer's roll is: {computerroll}")
    if userroll == 1: 
        userscore = 0 
        print(f"Oops {user}'s score is reset to 0")
    else: 
        userscore += userroll 
    if computerroll == 1: 
        computerscore = 0 
        print(f"Oops Computer's score is reset to 0")
    else: 
        computerscore += computerroll
    print(f"{user}'s score is: {userscore}")
    print(f"Computer's score is: {computerscore}")
    print("#" * 20)
    if userscore >= 30 or computerscore >= 30:
        break
if userscore > computerscore:
    print(f"Congrulations you won with a score of {userscore}!")
else:
    print(f"Oh no! Computer won with a score of {computerscore}")
