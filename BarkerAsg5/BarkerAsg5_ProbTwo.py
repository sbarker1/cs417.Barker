# Samuel Barker
# sbarker1@my.athens.edu
# CS 417 Assignment 5, Problem 2 Application

# References:
# https://www.geeksforgeeks.org/observer-method-python-design-patterns/#
# https://codereview.stackexchange.com/questions/20938/the-observer-design-pattern-in-python-with-unit-tests

# Define an abstract base class for the Subject and Observer classes in the Observer pattern.
class Subject:
    def __init__(self):
        self.observers = []  # Empty list to store registered observers.
        self.dictionary = {}  # Empty dictionary to store items.

    def register(self, observer):
        self.observers.append(observer)  # Register an observer by adding it to list.

    def unregister(self, observer):
        self.observers.remove(observer)  # Unregister an observer by removing it from list.

    def set_item(self, key, value):
        self.dictionary[key] = value  # Set an item in the dictionary.
        self.notify_all(key, value)  # Notify all registered observers.

    def notify_all(self, key, value):
        for observer in self.observers:
            observer.notify(key, value)  # Notify each registered observer.

# Define an abstract base class for Observers.
class Observer:
    def notify(self, key, value):
        pass  # An abstract method to be implemented by ConcreteObservers.

# Define a ConcreteSubject class, derived from Subject, where items are added to the dictionary.
class ConcreteSubject(Subject):
    def add_item(self, key, value):
        self.dictionary[key] = value  # Add an item to the dictionary.

# Define a ConcreteObserver class, derived from Observer, which will watch for changes in the dictionary.
class ConcreteObserver(Observer):
    def __init__(self, subject, name):
        self.name = name
        subject.register(self)  # Register this observer with the subject.

    def notify(self, key, value):
        print(f"{self.name} received an update: Key '{key}' has been changed to '{value}'")

if __name__ == "__main__":
    subject = ConcreteSubject()
    
    
    # Two ConcreteObserver objects and register them with the subject.
    observer1 = ConcreteObserver(subject, "Observer 1")
    observer2 = ConcreteObserver(subject, "Observer 2")

    # Add initial items to the subject dictionary.
    subject.add_item("item1", "value1")
    subject.add_item("item2", "value2")
    
    # Set new values for the items, triggering notifications to observers.
    subject.set_item("item1", "new_value1")
    subject.set_item("item2", "new_value2")
