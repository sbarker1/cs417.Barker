# Samuel Barker
# 00100768
# sbarker1@my.athens.edu
# Exam 3, Problem Three

# References:
# [1] https://www.geeksforgeeks.org/factory-method-python-design-patterns/#
# [2] https://realpython.com/factory-method-python/

# Note: please see the bottom to view FactoryMethod pattern modifications

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


class WidgetBuilder(Builder):
    def __init__(self):
        self.widget = Widget()

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 15
        self.widget.attachWheel(wheel)
        return wheel  # Add this line

    def getContainer(self):
        container = Container()
        container.volume = 10
        self.widget.setContainerVolume(container)
        return container  # Add this line

    def getBody(self):
        body = Body()
        body.shape = "Bucket"
        self.widget.setBody(body)
        return body  # Add this line

    def getResult(self):
        return self.widget


class AnotherWidgetBuilder(Builder):
    def __init__(self):
        self.widget = Widget()

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 20
        self.widget.attachWheel(wheel)
        return wheel  # Add this line

    def getContainer(self):
        container = Container()
        container.volume = 5
        self.widget.setContainerVolume(container)
        return container  # Add this line

    def getBody(self):
        body = Body()
        body.shape = "Glass"
        self.widget.setBody(body)
        return body  # Add this line

    def getResult(self):
        return self.widget

# WidgetFactory Modification [1]
class WidgetFactory:
    def createWidget(self, builder):
        builder.getWheel()
        builder.getContainer()
        builder.getBody()
        return builder.getResult()


# Modification - example... [2]
widget_factory = WidgetFactory()

widget_instance = widget_factory.createWidget(WidgetBuilder())

new_widget_instance = widget_factory.createWidget(AnotherWidgetBuilder())


# Print information about constructed widgets
print("Widget 1...")
print("Wheels:", [wheel.size for wheel in widget_instance.wheels])
print("Container volume:", widget_instance.container.volume)
print("Body Shape:", widget_instance.body.shape)

print("\nWidget 2...")
print("Wheels:", [wheel.size for wheel in new_widget_instance.wheels])
print("Container volume:", new_widget_instance.container.volume)
print("Body Shape:", new_widget_instance.body.shape)
