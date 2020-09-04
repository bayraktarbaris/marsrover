import unittest

from src import Plateau, Position, Rover


class TestPlateau(unittest.TestCase):
    def test_valid(self):
        plateau = Plateau(7, 10)

        self.assertEqual(plateau.width - 1, 7)
        self.assertEqual(plateau.height - 1, 10)

    def test_invalid_width(self):
        with self.assertRaises(ValueError) as e:
            width, height = -1, 10
            plateau = Plateau(width, height)

        self.assertEqual(type(e.exception), ValueError)
        self.assertEqual(str(e.exception), "Invalid width: {}".format(width))

    def test_invalid_height(self):
        with self.assertRaises(ValueError) as e:
            width, height = 10, -1
            plateau = Plateau(width, height)

        self.assertEqual(type(e.exception), ValueError)
        self.assertEqual(str(e.exception), "Invalid height: {}".format(height))

    def test___str__(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2)

        rover = Rover(plateau, position, 'N')
        self.assertEqual(str(rover.plateau), '0 0 0 0 0 0\n'
                                             '0 0 0 0 0 0\n'
                                             '0 0 0 0 0 0\n'
                                             '0 1 0 0 0 0\n'
                                             '0 0 0 0 0 0\n'
                                             '0 0 0 0 0 0\n')

    def test_move_not_available_north_boundary(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 10), 'N'
        self.assertEqual(plateau.move_available(position, heading), False)

    def test_move_not_available_south_boundary(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 0), 'S'
        self.assertEqual(plateau.move_available(position, heading), False)

    def test_move_not_available_west_boundary(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(0, 5), 'W'
        self.assertEqual(plateau.move_available(position, heading), False)

    def test_move_not_available_east_boundary(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(10, 5), 'E'
        self.assertEqual(plateau.move_available(position, heading), False)

    def test_move_available_north_inside(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 5), 'N'
        self.assertEqual(plateau.move_available(position, heading), True)

    def test_move_available_south_inside(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 5), 'S'
        self.assertEqual(plateau.move_available(position, heading), True)

    def test_move_available_west_inside(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 5), 'W'
        self.assertEqual(plateau.move_available(position, heading), True)

    def test_move_available_east_inside(self):
        width, height = 10, 10
        plateau = Plateau(width, height)
        position, heading = Position(5, 5), 'E'
        self.assertEqual(plateau.move_available(position, heading), True)


if __name__ == '__main__':
    unittest.main()
