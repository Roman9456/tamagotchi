import random
import schedule  # Модуль планировщик
import time

def rand_func():
    '''
    Выполняет функцию в случайном диапозоне времени от 1 сек. до 10 сек.
    '''
    print("Хочу есть ... ")


schedule.every(3).to(10).seconds.do(rand_func)

while True:
    schedule.run_pending()




# class Tamagotchi:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 50
#         self.health = 50
#         self.happiness = 50

#     def feed(self):
#         self.hunger -= 10
#         self.happiness += 10
#         self.check_limits()

#     def heal(self):
#         self.health += 10
#         self.happiness += 5
#         self.check_limits()

#     def play(self):
#         self.hunger += 10
#         self.happiness += 20
#         self.check_limits()

#     def check_limits(self):
#         if self.hunger > 100:
#             self.hunger = 100
#         elif self.hunger < 0:
#             self.hunger = 0

#         if self.health > 100:
#             self.health = 100
#         elif self.health < 0:
#             self.health = 0

#         if self.happiness > 100:
#             self.happiness = 100
#         elif self.happiness < 0:
#             self.happiness = 0

#     def status(self):
#         print(f"Имя: {self.name}")
#         print(f"Голод: {self.hunger}")
#         print(f"Здоровье: {self.health}")
#         print(f"Счастье: {self.happiness}")

# def main():
#     name = input("Введите имя тамагочи: ")
#     tamagotchi = Tamagotchi(name)

#     while True:
#         tamagotchi.status()

#         action = input("Что вы хотите сделать? (кормить, лечить, играть): ")

#         if action == "кормить":
#             tamagotchi.feed()
#         elif action == "лечить":
#             tamagotchi.heal()
#         elif action == "играть":
#             tamagotchi.play()
#         else:
#             print("Неизвестное действие")

#         if tamagotchi.happiness <= 0:
#             print("Тамагочи ушел в депрессию и умер...")
#             break
#         elif tamagotchi.hunger >= 100 or tamagotchi.health <= 0:
#             print("Тамагочи умер от голода или болезни...")
#             break

# if __name__ == "__main__":
#     main()