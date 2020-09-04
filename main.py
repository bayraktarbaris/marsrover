from src import Plateau
from src import Position
from src import Rover

"""
Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Output:
1 3 N
5 1 E
"""


def main():
    input_plateau = input().split()
    plateau_x, plateau_y = int(input_plateau[0]), int(input_plateau[1])
    plateau = Plateau(plateau_x, plateau_y)
    rovers = []
    while True:
        input_rover = input().split()
        if not input_rover:
            break
        rover_x, rover_y, heading = int(input_rover[0]), int(input_rover[1]), input_rover[2]
        position = Position(rover_x, rover_y)
        rover = Rover(plateau, position, heading)
        commands = input()
        rover.process(commands)
        rovers.append(rover)

    for rover in rovers:
        print(rover)

    # print("Plateau:")
    # print(plateau)


if __name__ == "__main__":
    main()
