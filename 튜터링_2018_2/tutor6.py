class Point:

    def __int__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __del__(self):
        print("Instance is removed")

def midpoint(p1, p2):
    mx = (p1.x + p2.x)/2
    my = (p1.x + p2.y)/2
    return Point(mx, my)

p = Point(3,4)
q = Point(4,5)
mp = midpoint(p, q)

print(mp)