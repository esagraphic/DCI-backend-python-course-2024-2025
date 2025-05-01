import math

class Point:
    def __init__(self):
        # self.x = 0  
        # self.y = 0  
        self.reset()

    def move(self, x, y):
        self.x = x  
        self.y = y  

    def reset(self):
        self.x = 0  
        self.y = 0  

    def calc_distance(self, other):
        """Calculate the distance between this point and another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

if __name__ == "__main__":
    p1 = Point()
    p2 = Point()

    p1.reset()
    p2.reset()

    print(p1.x, p1.y)  # Output: 0 0
    print(p2.x, p2.y)  # Output: 0 0

    p1.move(4, 7)
    p2.move(6, 2)

    print("After moving")
    print(p1.x, p1.y)  # Output: 4 7
    print(p2.x, p2.y)  # Output: 6 2

    # Calculate and print the distance between p1 and p2
    print("Distance between p1 and p2:", p1.calc_distance(p2))
