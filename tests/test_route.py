from unittest import TestCase, main
from plane.plane import Plane
from utils.route import build_route


class TestRoute(TestCase):
    def test_built_route(self):
        plane = Plane(5, 5)
        start_point = (0, 0)
        delivery_points = [(3, 2), (3, 3), (1, 0)]
        delivery_points_with_actions = [(point, ['D']) for point in delivery_points]
        expected_commands = ['N', 'N', 'E', 'E', 'E', 'D', 'N', 'D', 'S', 'S', 'S', 'W', 'W', 'D']
        commands = build_route(plane, delivery_points_with_actions, start_point)
        self.assertEqual(expected_commands, commands)
