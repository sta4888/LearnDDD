class Animal:  # сущность или домен ЖИВОТНОЕ
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Cage:  # сущность или домен КЛЕТКА
    def __init__(self, number):
        self.number = number
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)


class ZooService: # взаимодействие
    def __init__(self):
        self.animals = []

    def add_animal(self, name, species):
        animal = Animal(name, species)
        self.animals.append(animal)
        print(f"{name} ({species}) добавлен в зоопарк!")


if __name__ == '__main__':
    # Использование
    zoo = ZooService()
    zoo.add_animal("Лев", "Хищник")
