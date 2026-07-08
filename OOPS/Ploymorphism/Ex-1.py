class Shape:
    def draw(self):
        print("Drawing Shape")
    def erase(self):
        print("Erasing Shape")
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
    def erase(self):
        print("Erasing Circle")
class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")
    def erase(self):
        print("Erasing Triangle")
class Square(Shape):
    def draw(self):
        print("Drawing Square")
    def erase(self):
        print("Erasing Square")
shapes = [Circle(), Triangle(), Square()]
for s in shapes:
    s.draw()
    s.erase()