class Room:

    length = float(input("enter length: "))
    breadth = float(input("enter breadth: "))
    def Area(self):
        self.area = self.breadth * self.length
        print("Area: ", self.area)

o = Room()
o.Area()


