import traceback

from plane import Plane, OutOfPlane, ImpossibleMove, WrongGeometry
from utils.cmd import CMDParser
from utils.route import build_route, get_optimal_points_order, show_commands
from utils.point_with_action import PointWithActions

DROP_PIZZA = 'D'

if __name__ == '__main__':
    try:
        # Initializing plane
        parser = CMDParser()
        size_x, size_y = parser.field_size
        plane = Plane(size_x, size_y)

        # Adding actions to the delivery points
        delivery_points = get_optimal_points_order(parser.points)
        delivery_points_with_actions = [PointWithActions(point, [DROP_PIZZA]) for point in delivery_points]

        # Get and output the result
        commands = build_route(plane, delivery_points_with_actions)
        show_commands(commands)
    except WrongGeometry as e:
        print(e)
    except ImpossibleMove as e:
        print(e)
    except OutOfPlane as e:
        print(e)
    except Exception:
        with open('log.txt', 'w', encoding='utf-8') as f:
            traceback.print_exc(file=f)
        print('Ooops, something went wrong. See log.txt file to find out the details.')
