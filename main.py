class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height
    
    def get_name(self):
        return "Rectangle"
        
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * (self.__radius * self.__radius)
    
    def get_name(self):
        return "Circle"

class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def get_area(self):
        return (self.__base * self.__height) / 2
    
    def get_name(self):
        return "Triangle"



test_rectangle = Rectangle(5, 3)
test_circle = Circle(12)
triangle = Triangle(3, 12)

print(f"DEBUG: Triangle name = {triangle.get_name()}")