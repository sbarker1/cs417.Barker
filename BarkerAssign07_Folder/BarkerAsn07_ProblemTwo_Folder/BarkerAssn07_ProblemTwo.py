# Samuel Barker
# sbarker1@my.athens.edu
# Assignment 7, Problem 2

# Reference Citations:
# [1] https://www.geeksforgeeks.org/abstract-classes-in-python/#
# [2] https://pypi.org/project/xmlformatter/

# Abstraction for Shape
class Shape:   # [1]
    def __init__(self, formatter):
        self.formatter = formatter

    def draw(self):
        pass


# Concrete Shape classes , [1]
class Square(Shape):
    def draw(self):
        self.formatter.format("Square")

class Circle(Shape):
    def draw(self):
        self.formatter.format("Circle")

class Polygon(Shape): # Polygon class 
    def draw(self):
        self.formatter.format("Polygon")

# Abstraction for the Formatter
class Formatter:
    def format(self, shape_type):
        pass

# Concrete Formatter classes
class ScreenFormatter(Formatter):
    def format(self, shape_type):
        print(f"Drawing the {shape_type} on the screen...")

class PrinterFormatter(Formatter):
    def format(self, shape_type):
        print(f"Now, printing the {shape_type} on the printer...")

class XMLFormatter(Formatter):  # [2]  # XML Formatter class 
    def format(self, shape_type):
        print(f"Generating an XML for {shape_type}...")


# To demonstrate an example...

screen = ScreenFormatter()
printer = PrinterFormatter()
xml_formatter = XMLFormatter()

shape1 = Square(screen)
shape2 = Circle(printer)
shape3 = Polygon(xml_formatter)


shape1.draw()  #Output: Drawing the Square on the screen...
shape2.draw()  #Output: Now, printing Circle on the printer...
shape3.draw()  #Output: Generating an XML for Polygon...
