class Shape:
    def __init__(self, color=None):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return self.get_color() + ' Shape'


# Inheritance at PLay
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return self.get_color() + '' + str(self.length) + str(self.width) + ' ' + type(self).__name__


def print_shape_data(self):
    print('Shape:    ', type(self).__name__)
    print('Color:    ', self.get_color())
    print('Area :    ', self.get_area())
    print('Perimeter:', self.get_perimeter())


shape = Shape('red')
rectangle = Rectangle('red', 2, 4)
print_shape_data(rectangle)
print('Shape is ', shape.get_color())
print('area is ', rectangle.get_area())
