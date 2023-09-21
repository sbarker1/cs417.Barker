# Samuel Barker
# 00100768
# sbarker1@my.athens.edu
# CS 417, Exam 1, Problem 3

class FrequencyDistribution:
    def __init__(self, input_list):
        self.input_list = input_list
        self.frequency_table = {}

    # Method 1: Compute Freq Table
    def compute_frequency_table(self):
        for item in self.input_list:
            if item in self.frequency_table:
                self.frequency_table[item] += 1
            else:
                self.frequency_table[item] = 1

    # Method 2: Print Freq Table
    def print_frequency_table(self):
        if not self.frequency_table:
            print("Frequency table seems empty. Please compute it first.")
            return

        print("Element\tFrequency")
        for item, frequency in self.frequency_table.items():
            print(f"{item}\t{frequency}")

if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    
    fd = FrequencyDistribution(data)
    fd.compute_frequency_table()
    fd.print_frequency_table()
