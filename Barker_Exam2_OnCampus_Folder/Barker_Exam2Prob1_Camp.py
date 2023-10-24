# Samuel Barker
# sbarker1@my.athens.edu
# Exam 2 On-Campus, Problem 1

# References: 
# [1] https://cs.stanford.edu/people/nick/py/python-tuple.html
# [2] https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment

# [1]
def valueCalculation(x, y, z):
    x0, y0 = x # x0 = 3, y0 = 5
    x1, y1 = y # x1 = 6, y1 = 7
    z0, z1 = z # z0 = 8, z1 = 9

    # [2] 
    a = y1 - y0
    b = x0 - x1
    c = x0 * y1 - x1 * y0

    result = a * z0 + b * z1 - c
    return result

# Example input values
x = (3, 5)
y = (6, 7)
z = (8, 9)

result = valueCalculation(x, y, z)
print("The value is:", result)

