class Rover:
    DIRECTIONS = {
        'N': {'L': 'W', 'R': 'E'},
        'E': {'L': 'N', 'R': 'S'},
        'S': {'L': 'E', 'R': 'W'},
        'W': {'L': 'S', 'R': 'N'},
    }

    def __init__(self, plateau, position, heading):
        self.AVAILABLE_COMMANDS = {
            'M': self.move,
            'L': self.spin_left,
            'R': self.spin_right,
        }
        self.plateau = plateau
        self.position = position
        self.heading = heading
        self.plateau.visited[self.position.y][self.position.x] = True

    def __str__(self):
        return self.current_position

    @property
    def current_position(self):
        return '{} {} {}'.format(self.position.x, self.position.y, self.heading)

    def process(self, commands):
        for i in range(len(commands)):
            self.run_command(commands[i])

    def move(self):
        if not self.plateau.move_available(self.position, self.heading):
            raise Exception("Move not available")

        if self.heading == 'N':
            self.position.y += 1
        elif self.heading == 'E':
            self.position.x += 1
        elif self.heading == 'S':
            self.position.y -= 1
        elif self.heading == 'W':
            self.position.x -= 1

        self.plateau.visited[self.position.y][self.position.x] = True

        return True

    def spin_left(self):
        self.heading = self.DIRECTIONS[self.heading]['L']

    def spin_right(self):
        self.heading = self.DIRECTIONS[self.heading]['R']

    def run_command(self, command):
        if command not in self.AVAILABLE_COMMANDS.keys():
            raise Exception("Unrecognized command: {0}".format(command))

        try:
            self.AVAILABLE_COMMANDS[command]()
        except Exception as e:
            raise Exception("Can't move: {0}", e)
