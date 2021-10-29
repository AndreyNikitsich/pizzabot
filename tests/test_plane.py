from unittest import TestCase, main
from plane.plane import Plane
from plane.exeptions import WrongGeometry, ImpossibleMove, OutOfPlane


class TestPlane(TestCase):

    def test_init_raises_exception_if_geometry_is_invalid(self):
        wrong_geometry = {
            'key1': None,
            'key2': None,
        }
        with self.assertRaises(WrongGeometry):
            Plane(geometry=wrong_geometry)

    def test_init_ok_if_geometry_is_valid(self):
        right_geometry = {
            'moving_rules': None,
            'distance': None,
        }
        Plane(geometry=right_geometry)

    def test_contains_returns_true_if_point_is_on_plane(self):
        point = (1, 2)
        plane = Plane(5, 5)
        self.assertEqual(plane.contains(point), True)

    def test_contains_returns_false_if_point_is_out_of_plane(self):
        point = (11, 21)
        plane = Plane(15, 5)
        self.assertEqual(plane.contains(point), False)

    def test_get_neighbours_point_returns_neighbours_if_point_is_contained_on_plane(self):
        plane = Plane(5, 5)
        point = (2, 2)
        expected_neighbours = [(3, 2), (1, 2), (2, 3), (2, 1)]
        actual_neighbours = plane.get_neighbours_point(point)
        self.assertEqual(len(expected_neighbours), len(actual_neighbours))
        self.assertEqual(set(expected_neighbours), set(actual_neighbours))

    def test_get_neighbours_point_raises_exception_if_point_is_out_of_plane(self):
        plane = Plane(5, 5)
        point = (7, 2)
        with self.assertRaises(OutOfPlane):
            plane.get_neighbours_point(point)

    def test_convert_path_to_commands_returns_commands_if_path_is_valid(self):
        plane = Plane(5, 5)
        path = [(0, 1), (0, 2), (1, 2)]
        expected_commands = ['N', 'E']
        actual_commands = plane.convert_path_to_commands(path)
        self.assertEqual(expected_commands, actual_commands)

    def test_convert_path_to_commands_returns_no_commands_if_path_consists_of_one_point(self):
        plane = Plane(5, 5)
        path = [(2, 3)]
        expected_commands = []
        actual_commands = plane.convert_path_to_commands(path)
        self.assertEqual(expected_commands, actual_commands)

    def test_convert_path_to_commands_raises_exception_if_path_contains_point_that_is_out_of_plane(self):
        plane = Plane(5, 5)
        path = [(0, -1), (0, 0), (0, 1)]
        with self.assertRaises(OutOfPlane):
            plane.convert_path_to_commands(path)

    def test_convert_path_to_commands_raises_exception_if_move_from_one_point_to_another_is_impossible(self):
        plane = Plane(5, 5)
        path = [(2, 1), (0, 1), (1, 1)]
        with self.assertRaises(ImpossibleMove):
            plane.convert_path_to_commands(path)


if __name__ == '__main__':
    main()
