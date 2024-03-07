# make class for pet

class Pet():
    name = None
    fullness = 0
    food = None

    def __init__(self, name):
        self.name = name

    def eat (self, food):
        self.food = food
        print(self.name + "is eating" + food + "...")
        print(self.name + "is now" + self.fullness + "% full")

#start of program

pet_owner_name = input("What's your name?: ")
print ("Welcome " + pet_owner_name)
pet_1 = Pet("Rocky")
pet_1 = Pet.eat("carrots")
