#When it come to classes you dont use underscores, you capitalize the first letter of each word
#Simple types are numbers, strings, booleans, and complex types are lists and dictionaries
#These types above cannot be used to model complex concepts. So we can use classes to define new types to model real concepts


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point() #Note objects are instances of a class
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)