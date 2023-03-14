class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.__height = height

    def area(self):
        return self.width * self.__height

rect = Rectangle(5, 3)
rect.width = 10
rect.__height = 5

print(rect.area())
