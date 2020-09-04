import unittest

from src import Plateau, Position, Rover


class TestRover(unittest.TestCase):
    def test___str__(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        self.assertEqual(str(rover), '{} {} {}'.format(rover.position.x, rover.position.y, rover.heading))

    def test_current_position(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        self.assertEqual(rover.current_position, '{} {} {}'.format(rover.position.x, rover.position.y, rover.heading))

    def test_process(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        rover.process('LMLMLMLMM')

        self.assertEqual(rover.position, Position(1, 3))
        self.assertEqual(rover.heading, 'N')

    def move_not_available(self):
        plateau = Plateau(5, 5)
        position = Position(1, 8)
        initial_heading = 'N'
        rover = Rover(plateau, position, initial_heading)
        with self.assertRaises(Exception) as e:
            res = rover.move()

        self.assertEqual(type(e.exception), Exception)
        self.assertEqual(str(e.exception), "Move not available")

    def test_move_north(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        heading = 'N'
        rover = Rover(plateau, position, heading)
        self.assertEqual(rover.position, position)
        res = rover.move()
        self.assertEqual(res, True)
        self.assertEqual(rover.position, Position(1, 3))

    def test_move_south(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        heading = 'S'
        rover = Rover(plateau, position, heading)
        self.assertEqual(rover.position, position)
        res = rover.move()
        self.assertEqual(res, True)
        self.assertEqual(rover.position, Position(1, 1))

    def test_move_west(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        heading = 'W'
        rover = Rover(plateau, position, heading)
        self.assertEqual(rover.position, position)
        res = rover.move()
        self.assertEqual(res, True)
        self.assertEqual(rover.position, Position(0, 2))

    def test_move_east(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        heading = 'E'
        rover = Rover(plateau, position, heading)
        self.assertEqual(rover.position, position)
        res = rover.move()
        self.assertEqual(res, True)
        self.assertEqual(rover.position, Position(2, 2))

    def test_spin_left(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        initial_heading = 'N'
        rover = Rover(plateau, position, initial_heading)
        self.assertEqual(rover.heading, initial_heading)
        rover.spin_left()
        self.assertEqual(rover.heading, rover.DIRECTIONS[initial_heading]['L'])

    def test_spin_right(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)
        initial_heading = 'N'
        rover = Rover(plateau, position, initial_heading)
        self.assertEqual(rover.heading, initial_heading)
        rover.spin_right()
        self.assertEqual(rover.heading, rover.DIRECTIONS[initial_heading]['R'])

    def test_run_command_success(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        rover.run_command('L')

        self.assertEqual(rover.position, Position(1, 2))
        self.assertEqual(rover.heading, 'W')

    def test_run_command_unrecognized_command(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        command = 'A'
        with self.assertRaises(Exception) as e:
            rover.run_command(command)

        self.assertEqual(type(e.exception), Exception)
        self.assertEqual(str(e.exception), "Unrecognized command: {0}".format(command))


if __name__ == '__main__':
    unittest.main()
