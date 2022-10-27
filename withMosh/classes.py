from hashlib import new


class Point:
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")


newPoint = Point()

newPoint.draw()
newPoint.move()