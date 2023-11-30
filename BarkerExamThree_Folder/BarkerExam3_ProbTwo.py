# Samuel Barker
# 00100768
# sbarker1@my.athens.edu
# Exam 3, Problem Two

# References:
# [1] https://kivy.org/doc/stable/api-kivy.uix.widget.html
# [2] https://stackoverflow.com/questions/8915403/using-python-widget-classes

class Widget:
    def __init__(self):
        self.wheels = list()
        self.container = None
        self.body = None

    def attachWheel(self, wheel):
        self.wheels.append(wheel)

    def setContainerVolume(self, volume):
        self.container = volume

    def setBody(self, bodytype):
        self.body = bodytype

class Builder:
    def getWheel(self):
        pass

    def getContainer(self):
        pass

    def getBody(self):
        pass

class Wheel:
    size = None

class Container:
    volume = None

class Body:
    shape = None

class WidgetBuilder(Builder): # Subclass 1 [1]
    def __init__(self):
        self.widget = Widget()

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 15  # To test, let's set a default size for this wheel.
        self.widget.attachWheel(wheel)

    def getContainer(self):
        container = Container()
        container.volume = 10  # default volume for this container
        self.widget.setContainerVolume(container)

    def getBody(self):
        body = Body()
        body.shape = "Bucket"  # default shape for this body
        self.widget.setBody(body)

    def getResult(self):
        return self.widget

class AnotherWidgetBuilder(Builder): # Subclass 2 [1], [2]
    def __init__(self):
        self.widget = Widget()

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 20  # Set different size for the wheel
        self.widget.attachWheel(wheel)

    def getContainer(self):
        container = Container()
        container.volume = 5  # Set a different volume for the container
        self.widget.setContainerVolume(container)

    def getBody(self):
        body = Body()
        body.shape = "Glass"  # Set different shape for the body
        self.widget.setBody(body)

    def getResult(self):
        return self.widget

widget_builder = WidgetBuilder()
widget_builder.getWheel()
widget_builder.getContainer()
widget_builder.getBody()
widget_instance = widget_builder.getResult()

newWidgetBuilder = AnotherWidgetBuilder()
newWidgetBuilder.getWheel()
newWidgetBuilder.getContainer()
newWidgetBuilder.getBody()
newWidgetInstance = newWidgetBuilder.getResult()

# Print information about constructed widgets 1 and 2.
print("Widget 1...")
print("Wheels:", [wheel.size for wheel in widget_instance.wheels])
print("Container volume:", widget_instance.container.volume)
print("Body Shape:", widget_instance.body.shape)


# Now for widget 2 print out
print("\nWidget 2...")
print("Wheels:", [wheel.size for wheel in newWidgetInstance.wheels])
print("Container volume:", newWidgetInstance.container.volume)
print("Body Shape:", newWidgetInstance.body.shape)
