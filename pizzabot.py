import plane
from plane import Plane
from utils.cmd import CMDParser
from utils.route import build_route, get_optimal_route_order

DROP_PIZZA = 'D'

if __name__ == '__main__':
    try:
        parser = CMDParser.get_parser()
        args = parser.parse_args()
        size_x, size_y = args.field_size
        pl = Plane(size_x, size_y)
        delivery_points = get_optimal_route_order(args.points)
        delivery_points_with_actions = [(point, [DROP_PIZZA]) for point in delivery_points]
        commands = build_route(pl, delivery_points_with_actions)
        print(commands)
    except plane.OutOfPlane as e:
        print(f'Point {e} out of plane {size_x}x{size_y}')
    except Exception as e:
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(e)
        print('Ooops, something went wrong. See log file to find out the details.')
