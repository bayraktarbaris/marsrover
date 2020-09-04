class Position:
    def __init__(self, x=0, y=0):
        if x < 0:
            raise ValueError("Invalid x: {0}".format(x))
        if y < 0:
            raise ValueError("Invalid y: {0}".format(y))
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y
