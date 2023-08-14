class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: int):
        # Provide the side as width and height for the
        # superclass constructor
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.width}"


# 这里不call area method 的原因是因为：you haven't overridden the area() method in the Square class. Instead, you're relying on the area() method inherited from the Rectangle class.
if __name__ == "__main__":
    square = Square(4)
    print(square)
    print("area:", square.area())
