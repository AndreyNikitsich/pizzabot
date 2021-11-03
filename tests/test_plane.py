from unittest import TestCase, main
from plane.plane import Plane
from plane.exeptions import WrongGeometry, ImpossibleMove, OutOfPlane


class TestPlane(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.plane = Plane(5, 5)

    def test_init_raises_wrong_geometry(self):
        wrong_geometry = {
            'key1': None,
            'key2': None,
        }
        with self.assertRaises(WrongGeometry):
            Plane(geometry=wrong_geometry)

    def test_init_with_valid_geometry(self):
        right_geometry = {
            'moving_rules': None,
            'distance': None,
        }
        Plane(geometry=right_geometry)

    def test_contains_with_valid_point(self):
        """Valid point is a point that is on the plane."""

        point = (1, 2)
        self.assertEqual(self.plane.contains(point), True)

    def test_contains_with_invalid_point(self):
        """Invalid point is a point that is not on the plane."""

        point = (11, 21)
        self.assertEqual(self.plane.contains(point), False)

    def test_get_neighbours_point_with_valid_point(self):
        """Valid point is a point that is on the plane."""

        point = (2, 2)
        expected_neighbours = [(3, 2), (1, 2), (2, 3), (2, 1)]
        actual_neighbours = self.plane.get_neighbours_point(point)
        self.assertEqual(len(expected_neighbours), len(actual_neighbours))
        self.assertEqual(set(expected_neighbours), set(actual_neighbours))

    def test_get_neighbours_point_raises_out_of_plane(self):
        point = (7, 2)
        with self.assertRaises(OutOfPlane):
            self.plane.get_neighbours_point(point)

    def test_convert_path_to_commands_with_average_path(self):
        """Average path is a path consisting of more than one point."""

        path = [(0, 1), (0, 2), (1, 2)]
        expected_commands = ['N', 'E']
        actual_commands = self.plane.convert_path_to_commands(path)
        self.assertEqual(expected_commands, actual_commands)

    def test_convert_path_to_commands_with_path_consists_of_one_point(self):
        path = [(2, 3)]
        expected_commands = []
        actual_commands = self.plane.convert_path_to_commands(path)
        self.assertEqual(expected_commands, actual_commands)

    def test_convert_path_to_commands_raises_out_of_plane(self):
        path = [(0, -1), (0, 0), (0, 1)]
        with self.assertRaises(OutOfPlane):
            self.plane.convert_path_to_commands(path)

    def test_convert_path_to_commands_raises_impossible_move(self):
        path = [(2, 1), (0, 1), (1, 1)]
        with self.assertRaises(ImpossibleMove):
            self.plane.convert_path_to_commands(path)
