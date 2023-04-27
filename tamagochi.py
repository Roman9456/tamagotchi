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
