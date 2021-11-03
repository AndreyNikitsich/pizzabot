from plane import bfs_path, Point, Plane
from utils.point_with_action import PointWithActions


def build_route(plane: Plane, delivery_points_with_actions: list[PointWithActions],
                start_point: Point = (0, 0)) -> list[str]:
    """Return a list of commands required to move from the starting point through all delivery points."""
    route_points = [PointWithActions(start_point, [])] + delivery_points_with_actions
    commands = []
    for i in range(1, len(route_points)):
        point_from = route_points[i - 1].point
        point_to, actions = route_points[i].point, route_points[i].actions
        path = bfs_path(plane, point_from, point_to)
        commands += plane.convert_path_to_commands(path)
        commands += actions
    return commands


def get_optimal_points_order(point_list: list[Point]) -> list[Point]:
    """Return a sequence of points in the order that provides the shortest path length."""

    # we must solve the TSP problem to find shortest path between points.
    # There are so many methods to do this, but implementing one of them is out of scope, I think ;)

    return point_list


def show_commands(commands_list: list[str]) -> None:
    """Output a list of commands to the console with the required formatting."""
    output_string = ''.join(commands_list)
    print(output_string)
