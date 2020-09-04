import copy


class Plateau(object):
    MIN_WIDTH = 0
    MIN_HEIGHT = 0

    def __init__(self, width, height, min_width=0, min_height=0):
        if width < 1:
            raise ValueError("Invalid width: {0}".format(width))
        if height < 1:
            raise ValueError("Invalid height: {0}".format(height))
        self.width = width + 1
        self.height = height + 1
        self.MIN_WIDTH = min_width
        self.MIN_HEIGHT = min_height
        self.visited = [[False for i in range(self.width)] for j in range(self.height)]

    def __str__(self):
        res = ""
        for row in reversed(self.visited):
            res += " ".join(list(map(lambda x: '1' if x else '0', row)))
            res += "\n"

        return res

    def move_available(self, position, heading):
        tmp_position = copy.deepcopy(position)
        if 'N' == heading:
            tmp_position.y += 1
        elif 'E' == heading:
            tmp_position.x += 1
        elif 'S' == heading:
            tmp_position.y -= 1
        elif 'W' == heading:
            tmp_position.x -= 1

        return self.MIN_WIDTH <= tmp_position.x < self.width and self.MIN_HEIGHT <= tmp_position.y < self.height
