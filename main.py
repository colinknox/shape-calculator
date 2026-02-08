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



test_rectangle = Rectangle(5, 3)
test_circle = Circle(12)

# print(f"DEBUG: Get area = {test_circle.get_area()}")
print(f"DEBUG: Get name = {test_circle.get_name()}")