import plane
from plane import Plane
from cmd import parser

DROP_PIZZA = 'D'


def build_route(plane, delivery_points_with_actions, start_point=(0, 0)):
    route_points = [(start_point, [])] + delivery_points_with_actions
    commands = []
    for i in range(1, len(route_points)):
        point_1, action_1 = route_points[i - 1]
        point_2, action_2 = route_points[i]
        path = plane.bfs_path(point_1, point_2)
        commands += plane.convert_path_to_commands(path)
        commands += action_2
    return commands


def optimal_order(point_list):
    # we must solve the TSP problem to find shortest path between points.
    # There are so many methods to do this, but implementing one of them is out of scope, I think ;)
    return point_list


if __name__ == '__main__':
    try:
        args = parser.parse_args()
        size_x, size_y = args.field_size
        pl = Plane(size_x, size_y)
        delivery_points = optimal_order(args.points)
        delivery_points_with_actions = [(point, [DROP_PIZZA]) for point in delivery_points]
        commands = build_route(pl, delivery_points_with_actions)
        print(commands)
    except plane.OutOfPlane as e:
        print(f'Point {e} out of plane {size_x}x{size_y}')
    except Exception as e:
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(e)
        print('Ooops, something went wrong. See log file to find out the details.')
