from unittest import TestCase, main
from plane.plane import Plane
from plane.exeptions import OutOfPlane
from plane.algorithms import bfs_path


class TestAlgorithms(TestCase):

    def test_bfs_path_with_valid_points(self):
        """Valid point is a point that is on the plane."""

        plane = Plane(5, 5)
        start_point = (0, 0)
        end_point = (2, 1)
        possible_paths = [[(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, 1), (2, 1)],
                          [(0, 0), (1, 0), (2, 0), (2, 1)]]
        actual_path = bfs_path(plane, start_point, end_point)
        self.assertIn(actual_path, possible_paths)

    def test_bfs_path_raises_out_of_plane(self):
        plane = Plane(5, 5)
        start_point = (-1, -1)
        end_point = (2, 1)
        with self.assertRaises(OutOfPlane):
            bfs_path(plane, start_point, end_point)


