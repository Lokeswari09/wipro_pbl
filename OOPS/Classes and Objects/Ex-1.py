class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_volume(self):
        return self.width * self.height * self.depth

w = float(input("Enter width: "))
h = float(input("Enter height: "))
d = float(input("Enter depth: "))

my_box = Box(w, h, d)
print("Volume of the box is:", my_box.get_volume())