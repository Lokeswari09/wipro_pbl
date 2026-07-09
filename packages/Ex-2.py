class Compartment:
    def __init__(self, height, width, breadth):
        self.height = height
        self.width = width
        self.breadth = breadth

    def get_dimensions(self):
        return f"Dimensions: {self.height}x{self.width}x{self.breadth}"