#!/usr/bin/python3

class Square():
    
    def __init__(self, width=0, height=0):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative values")
        self.width = width
        self.height = height

    def area(self):
        """ Calculate the area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Calculate the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "Square - Width: {}, Height: {}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

