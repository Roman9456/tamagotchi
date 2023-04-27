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
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0

        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0

        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Голод: {self.hunger}")
        print(f"Здоровье: {self.health}")
        print(f"Счастье: {self.happiness}")


class Cat(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Мяу"
        self.species = "Кошка"

    def make_sound(self):
        print(self.sound)


class Dog(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Гав"
        self.species = "Собака"

    def make_sound(self):
        print(self.sound)


class Parrot(Tamagotchi):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Кар-кар"
        self.species = "Попугай"

    def make_sound(self):
        print(self.sound)


def main():
    animal = input("Выберите животное (кот, собака, попугай): ")

    if animal == "кот":
        name = input("Введите имя кота: ")
        pet = Cat(name)
    elif animal == "собака":
        name = input("Введите имя собаки: ")
        pet = Dog(name)
    elif animal == "попугай":
        name = input("Введите имя попугая: ")
        pet = Parrot(name)
    else:
        print("Неизвестное животное")
        return

    while True:
        pet.status()

        action = input("Что вы хотите сделать? (кормить, лечить, играть): ")

        if action == "кормить":
            pet.feed()
        elif action == "лечить":
            pet.heal()
        elif action == "играть":
            pet.play()
        else:
            print("Неизвестное действие")

        if pet.happiness <= 0:
            print(f"{pet.species} {pet.name} ушел в депрессию и умер...")
            break
        elif pet.hunger >= 100 or pet.health <= 0:
            print(f"{pet.species} {pet.name} умер от голода или болезни...")
            break

    print("Игра окончена.")

if __name__ == "__main__":
    main()
