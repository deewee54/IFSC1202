class Pet:
    def __init__(self):
        self.Name = ""
        self.Type = "" 
        self.Age = "0"

pets =[]
file = open("10.01 Pets.txt", "r")
lines = file.readlines()
file.close()

for line in lines: 
    name, pet_type, age = line.strip().split(", ")
    pet = Pet()
    pet.Name = name 
    pet.Type = pet_type 
    pet.Age = int(age)
    pets.append(pet)

print("{:<7} {:<7} {:<4}".format("Name", "Type", "Age"))

for pet in pets: 
    print("{:<8} {:<8} {:<5}".format(pet.Name, pet.Type, pet.Age))

