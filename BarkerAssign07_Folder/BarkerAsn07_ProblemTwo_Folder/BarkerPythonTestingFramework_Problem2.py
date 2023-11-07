# Samuel Barker
# sbarker1@my.athens.edu
# Assignment 7, Problem 2 Test Framework Source

# Reference Citations:
# [1] https://docs.python.org/3/library/unittest.html
# [2] https://www.browserstack.com/guide/unit-testing-python

import unittest # [1]

# Importing my original source...
from BarkerAssn07_ProblemTwo import Square, Circle, Polygon, ScreenFormatter, PrinterFormatter, XMLFormatter

class TestShapeDrawing(unittest.TestCase): # [2]
    def test_square_drawing(self):
        screen = ScreenFormatter()
        shape = Square(screen)
        self.assertEqual(shape.draw(), "Drawing the Square on the screen...")

    def test_circle_printing(self):
        printer = PrinterFormatter()
        shape = Circle(printer)
        self.assertEqual(shape.draw(), "Now, printing Circle on the printer...")

    def test_polygon_xml_generation(self):
        xml_formatter = XMLFormatter()
        shape = Polygon(xml_formatter)
        self.assertEqual(shape.draw(), "Generating an XML for Polygon...")

if __name__ == '__main__':
    unittest.main()
