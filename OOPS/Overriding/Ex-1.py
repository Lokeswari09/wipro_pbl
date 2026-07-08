class Fruit:
    def __init__(self, name, taste, size):
        self.name = name
        self.taste = taste
        self.size = size
    def eat(self):
        print(f"Eating {self.name} which is {self.taste}")
class Apple(Fruit):
    def __init__(self, taste, size):
        super().__init__("Apple", taste, size)
    def eat(self):
        print(f"Crunching into a sweet {self.name} of {self.size} size")
class Orange(Fruit):
    def __init__(self, taste, size):
        super().__init__("Orange", taste, size)
    def eat(self):
        print(f"Peeling a juicy {self.name} which is {self.taste}")
f_name = input()
f_taste = input()
f_size = input()
if f_name.lower() == "apple":
    fruit = Apple(f_taste, f_size)
elif f_name.lower() == "orange":
    fruit = Orange(f_taste, f_size)
else:
    fruit = Fruit(f_name, f_taste, f_size)
fruit.eat()