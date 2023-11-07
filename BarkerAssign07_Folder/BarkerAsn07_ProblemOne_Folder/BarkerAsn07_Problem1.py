# Samuel Barker
# sbarker1@my.athens.edu
# Assignment 7, Problem 1 

# Reference Citations:
# [1] https://introcs.cs.princeton.edu/python/15inout/
# [2] https://realpython.com/beginners-guide-python-turtle/

class Square:
    def __init__(self, number, length, x, y):
        self.number = number
        self.length = length
        self.x = x
        self.y = y

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class CreateCommand(Command):
    def __init__(self, square, squares):
        self.square = square # [1]
        self.squares = squares

    def execute(self):
        self.squares.append(self.square)

    def undo(self):
        self.squares.remove(self.square)

class MoveCommand(Command):
    def __init__(self, square, new_x, new_y):
        self.square = square # [1]
        self.new_x = new_x
        self.new_y = new_y
        self.old_x = square.x
        self.old_y = square.y

    def execute(self):
        self.square.x = self.new_x
        self.square.y = self.new_y

    def undo(self):
        self.square.x = self.old_x
        self.square.y = self.old_y

class ScaleCommand(Command):
    def __init__(self, square, factor):
        self.square = square
        self.factor = factor
        self.old_length = square.length

    def execute(self):
        self.square.length *= self.factor

    def undo(self):
        self.square.length = self.old_length

class History:
    def __init__(self):
        self.commands = []
        self.current_index = -1

    def execute(self, command):
        if self.current_index < len(self.commands) - 1:
            del self.commands[self.current_index + 1:]
        command.execute()
        self.commands.append(command)
        self.current_index += 1

    def undo(self):
        if self.current_index >= 0:
            self.commands[self.current_index].undo()
            self.current_index -= 1

    def redo(self):
        if self.current_index < len(self.commands) - 1:
            self.current_index += 1
            self.commands[self.current_index].execute()


# Main 
squares = []
history = History()

while True:
    command = input("Enter a command (use spaces to enter separate values): ").split()  # [2]
    if command[0] == 'C': # Create a square
        number, length = int(command[1]), int(command[2])
        square = Square(number, length, 0, 0)
        cmd = CreateCommand(square, squares)
        history.execute(cmd)
    elif command[0] == 'M': # Move square
        number, new_x, new_y = int(command[1]), int(command[2]), int(command[3])
        square = next((s for s in squares if s.number == number), None)
        if square:
            cmd = MoveCommand(square, new_x, new_y)
            history.execute(cmd)
    elif command[0] == 'S': # Scaling square
        number, factor = int(command[1]), float(command[2])
        square = next((s for s in squares if s.number == number), None)
        if square:
            cmd = ScaleCommand(square, factor)
            history.execute(cmd)
    elif command[0] == 'U': # Undo last command mentioned. 
        history.undo()
    elif command[0] == 'R': # Redo 
        history.redo()
    elif command[0] == 'P': # Print out stats for all squares. 
        for square in squares:
            print(f"({square.number},{square.x},{square.y},{square.length})")
    elif command[0] == 'X': # Exit program
        break
