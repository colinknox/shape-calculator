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
        return 3.14159 * (self.__radius ** 2)
    
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

def calculate_total_area(shapes):
    total_area = 0
    
    for current_shape in shapes:
        print(f"{current_shape.get_name()}: {current_shape.get_area()} square units")
        total_area += current_shape.get_area()

    return total_area