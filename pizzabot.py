import traceback

from plane import Plane, OutOfPlane, ImpossibleMove, WrongGeometry
from utils.cmd import CMDParser
from utils.route import build_route, get_optimal_route_order

DROP_PIZZA = 'D'

if __name__ == '__main__':
    try:
        parser = CMDParser.get_parser()
        args = parser.parse_args()
        size_x, size_y = args.field_size
        plane = Plane(size_x, size_y)
        delivery_points = get_optimal_route_order(args.points)
        delivery_points_with_actions = [(point, [DROP_PIZZA]) for point in delivery_points]
        commands = build_route(plane, delivery_points_with_actions)
        output = ''.join(commands)
        print(output)
    except WrongGeometry as e:
        print(e)
    except ImpossibleMove as e:
        print(e)
    except OutOfPlane as e:
        print(e)
    except Exception as e:
        with open('log.txt', 'w', encoding='utf-8') as f:
            traceback.print_exc(file=f)
        print('Ooops, something went wrong. See log.txt file to find out the details.')
