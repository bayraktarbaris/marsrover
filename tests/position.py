import unittest

from src import Position


class TestPosition(unittest.TestCase):
    def test_empty_position(self):
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

    def test_position(self):
        position = Position(10, 20)
        self.assertEqual(position.x, 10)
        self.assertEqual(position.y, 20)

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as e:
            x, y = -1, 10
            position = Position(x, y)

        self.assertEqual(type(e.exception), ValueError)
        self.assertEqual(str(e.exception), "Invalid x: {}".format(x))

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as e:
            x, y = 10, -1
            position = Position(x, y)

        self.assertEqual(type(e.exception), ValueError)
        self.assertEqual(str(e.exception), "Invalid y: {}".format(y))

    def test_eq(self):
        x, y = 10, 10
        position = Position(x, y)
        position_other = Position(x, y)
        self.assertEqual(position, position_other)

    def test_not_eq(self):
        x, y = 10, 10
        position = Position(x, y)
        x_other, y_other = 5, 5
        position_other = Position(x_other, y_other)
        self.assertNotEqual(position, position_other)


if __name__ == '__main__':
    unittest.main()
