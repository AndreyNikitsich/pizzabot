from plane import bfs_path


def build_route(plane, delivery_points_with_actions, start_point=(0, 0)) -> list:
    route_points = [(start_point, [])] + delivery_points_with_actions
    commands = []
    for i in range(1, len(route_points)):
        point_1, action_1 = route_points[i - 1]
        point_2, action_2 = route_points[i]
        path = bfs_path(plane, point_1, point_2)
        commands += plane.convert_path_to_commands(path)
        commands += action_2
    return commands


def get_optimal_route_order(point_list):
    # we must solve the TSP problem to find shortest path between points.
    # There are so many methods to do this, but implementing one of them is out of scope, I think ;)
    return point_list
