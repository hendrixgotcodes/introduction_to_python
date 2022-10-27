
class Point:

    def _init_(self, x,y):
        self.x = x
        self.y = y
    
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")


newPoint = Point()

newPoint.draw()
newPoint.move()