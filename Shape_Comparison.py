class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.area() > other.area()


box1 = Box(3, 4)
box2 = Box(2, 5)
print(box1 > box2)       # True