from math import inf
from typing import Union

from .exeptions import OutOfPlane, ImpossibleMove, WrongGeometry
from .geometrics import TAXI_CUB_GEOMETRY

Point = tuple[int, int]


class Plane:

    def __init__(self, size_x: int = inf, size_y: int = inf, geometry: dict = None):
        self._size_x = size_x
        self._size_y = size_y

        if geometry is None:
            geometry = TAXI_CUB_GEOMETRY

        if 'distance' not in geometry.keys() or 'moving_rules' not in geometry.keys():
            raise WrongGeometry('The geometry must has \'distance\' and \'moving_rules\' keys')

        self._geometry = geometry
        self._moving_rules = geometry['moving_rules']
        self._distance_func = geometry['distance']

    def contains(self, point: Point) -> bool:
        """Checks whether a point is contained in the plane."""
        x, y = point
        return 0 <= x < self._size_x and 0 <= y < self._size_y

    def get_neighbours_point(self, point: Point) -> list[Point]:
        """Returns valid neighbours for point. Valid ones are those that are contained on the plane."""
        if not self.contains(point):
            raise OutOfPlane(point, self)

        neighbours = [(self.__add_points(point, rule)) for rule in self._moving_rules.keys()]
        valid_neighbours = filter(self.contains, neighbours)
        return list(valid_neighbours)

    def get_distance_between_points(self, first: Point, second: Point) -> Union[int, float]:
        """Returns distance between 2 point depending on the specified geometry."""
        if not self.contains(first):
            raise OutOfPlane(first, self)

        if not self.contains(second):
            raise OutOfPlane(first, self)

        return self._distance_func(first, second)

    @staticmethod
    def __subtract_points(first: Point, second: Point) -> Point:
        x_first, y_first = first
        x_second, y_second = second
        return x_first - x_second, y_first - y_second

    @staticmethod
    def __add_points(first: Point, second: Point) -> Point:
        x_first, y_first = first
        x_second, y_second = second
        return x_first + x_second, y_first + y_second

    def __get_move_direction(self, from_p: Point, to_p: Point) -> Point:
        """Returns the direction of movement for moving from one point to another."""
        move_direction_raw_value = self.__subtract_points(to_p, from_p)
        try:
            move_direction = self._moving_rules[move_direction_raw_value]
        except KeyError:
            raise ImpossibleMove(f'Impossible move for current rules: {from_p} -> {to_p}, rules: {self._moving_rules}')
        return move_direction

    def convert_path_to_commands(self, path: list) -> list:
        """Returns a sequence of commands to move from the start point of the path to the end of the path."""
        commands = []
        for i in range(1, len(path)):

            if not self.contains(path[i - 1]):
                raise OutOfPlane(path[i - 1], self)

            if not self.contains(path[i]):
                raise OutOfPlane(path[i], self)

            direction = self.__get_move_direction(path[i - 1], path[i])
            commands.append(direction)
        return commands

    def __str__(self):
        return f'Plane {self._size_x}x{self._size_y}'
