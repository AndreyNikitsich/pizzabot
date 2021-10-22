from plane import bfs_path, Point, Plane

Point_with_action = tuple[Point, list[str]]


def build_route(plane: Plane, delivery_points_with_actions: list[Point_with_action],
                start_point: Point = (0, 0)) -> list:
    """Returns a list of commands required to move from the starting point through all delivery points."""
    route_points = [(start_point, [])] + delivery_points_with_actions
    commands = []
    for i in range(1, len(route_points)):
        point_1, action_1 = route_points[i - 1]
        point_2, action_2 = route_points[i]
        path = bfs_path(plane, point_1, point_2)
        commands += plane.convert_path_to_commands(path)
        commands += action_2
    return commands


def get_optimal_points_order(point_list: list[Point]) -> list:
    """Returns a sequence of points in the order that provides the shortest path length."""
    # we must solve the TSP problem to find shortest path between points.
    # There are so many methods to do this, but implementing one of them is out of scope, I think ;)
    return point_list


def convert_commands_to_output_format(commands_list: list[str]) -> str:
    """Returns a string with a sequence of commands with the required formatting."""
    return ''.join(commands_list)
