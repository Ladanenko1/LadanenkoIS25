#  Создайте класс "Фрукт", который содержит информацию о наименовании и весе
# фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
# "Фрукт" и содержат информацию о цвет
class Fruit:
    def init(self, name, weight):
        self.name = name
        self.weight = weight

class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().init(name, weight)
        self.color = color

class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().init(name, weight)
        self.color = color

apple = Apple("сися", 150, "зеленый")
orange = Orange("абоба", 200, "оранжевый")
print(apple.name, apple.weight, apple.color)
print(orange.name, orange.weight, orange.color)
