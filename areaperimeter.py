class Circle:
    def __init__(self, list):
        self.pi = 3.1413  # private variable
        self.list = list

    def area(self):
        areas = [self.pi * radius * radius for radius in self.list]
        return areas

    def perimeter(self):
        perimeters = [2 * self.pi * radius for radius in self.list]
        return perimeters

#list
list = [10, 501, 22, 37, 100, 999, 87, 351]

# Creating an instance of the Circle class
obj = Circle(list)

# Calculating and printing the areas and perimeters of circle
areas = obj.area()
perimeters = obj.perimeter()

print("Area of circle with radius given in list ",obj.area())
print("Perimeter of circle with radius given in list ",obj.perimeter())


