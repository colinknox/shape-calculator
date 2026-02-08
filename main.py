class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height
    
    def get_name(self):
        return "Rectangle"
        


test_rectangle = Rectangle(5, 3)

print(f"DEBUG: Area = {test_rectangle.get_area()}")
print(f"DEBUG: Name = {test_rectangle.get_name()}")
print(f"DEBUG: Width and height = {test_rectangle.get_width_and_height()}")