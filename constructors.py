class Point:
    def __init__(self, x, y): #A Constructor
        self.x = x
        self.y = y


    def move(self):
        print("move")


    def draw(self):
        print("draw")



 point = Point(10, 20) #A constructor is a function that gets called at the time of creating an object
 print(point.x)