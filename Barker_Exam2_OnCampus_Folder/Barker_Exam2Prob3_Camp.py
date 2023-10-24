# Samuel Barker
# sbarker1@my.athens.edu
# Exam 2 On-Campus, Problem 3

# References: 
# [1] https://stackoverflow.com/questions/74812556/computing-quick-convex-hull-using-numba
# [2] https://math.stackexchange.com/questions/4463920/at-least-3-points-on-the-convex-hull#:~:text=If%20there%20are%20two%20extreme,of%20the%20closed%20convex%20hull.
# [3] https://medium.com/100-days-of-algorithms/day-28-convex-hull-bc84b678da06
# [4] https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda

def type(p, q, r): # [1]
    # Providing a helper function to see the type or type of three points.
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def convexHull(points): # [3]
    n = len(points)

    if n < 3:
        # Recognized the Convex hull having 3 extreme points, [2]
        return points
    
    min_point = min(points, key=lambda p: (p[1], p[0]))
    
    hull = []
    current_point = min_point
    
    while True: # [3]
        hull.append(current_point)
        next_point = (current_point[0] + 1, current_point[1])
        
        for p in points:
            if p == current_point:
                continue
            type_val = type(current_point, next_point, p)


            if type_val == -1 or (type_val == 0 and p != current_point):
                next_point = p
       
        if next_point == min_point:
            break
        
        current_point = next_point
    
    # Sort the convex hull points by given coordinates
    sorted_hull_points = sorted(hull, key=lambda p: (p[0], p[1])) # [4]
    
    return sorted_hull_points

# Read data points from the file from last question...
with open('C:/Users/erbab/Desktop/e2p2data.csv', 'r') as file:
    points = [tuple(map(int, line.strip().split(','))) for line in file]


convex_hull_points = convexHull(points)
print(convex_hull_points)
