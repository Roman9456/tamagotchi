class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.health = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 10
        self.check_limits()

    def heal(self):
        self.health += 10
        self.happiness += 5
        self.check_limits()

    def play(self):
        self.hunger += 10
        self.happiness += 20
        self.check_limits()

    def check_limits(self):
        self.hunger = max(0, min(100, self.hunger))
        self.health = max(0, min(100, self.health))
        self.happiness = max(0, min(100, self.happiness))

    def status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")


class Cat(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Meow"
        self.species = "Cat"

    def make_sound(self):
        print(self.sound)


class Dog(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof"
        self.species = "Dog"

    def make_sound(self):
        print(self.sound)


class Parrot(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Squawk"
        self.species = "Parrot"

    def make_sound(self):
        print(self.sound)


def main():
    animal = input("Choose an animal (cat, dog, parrot): ")

    if animal == "cat":
        name = input("Enter the cat's name: ")
        pet = Cat(name)
    elif animal == "dog":
        name = input("Enter the dog's name: ")
        pet = Dog(name)
    elif animal == "parrot":
        name = input("Enter the parrot's name: ")
        pet = Parrot(name)
    else:
        print("Unknown animal")
        return

    while True:
        pet.status()

        action = input("What would you like to do? (feed, heal, play): ")

        if action == "feed":
            pet.feed()
        elif action == "heal":
            pet.heal()
        elif action == "play":
            pet.play()
        else:
            print("Unknown action")

        if pet.happiness <= 0:
            print(f"{pet.species} {pet.name} fell into depression and died...")
            break
        elif pet.hunger >= 100 or pet.health <= 0:
            print(f"{pet.species} {pet.name} died of hunger or illness...")
            break

    print("Game over.")


if __name__ == "__main__":
    main()