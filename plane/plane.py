from collections import deque
from math import inf
from typing import Union

from .exeptions import OutOfPlane, ImpossibleMove
from .geometrics import TAXI_CUB_GEOMETRY

Point = tuple[int, int]


class Plane:

    def __init__(self, size_x: int = inf, size_y: int = inf, geometry: dict = None):
        self._size_x = size_x
        self._size_y = size_y
        if geometry is None:
            geometry = TAXI_CUB_GEOMETRY

        if 'distance' not in geometry.keys() or 'moving_rules' not in geometry.keys():
            raise NotImplemented('The geometry must has \'distance\' and \'moving_rules\' keys')
        self._geometry = geometry
        self._moving_rules = geometry['moving_rules']
        self._distance_func = geometry['distance']

    def contain(self, point: Point) -> bool:
        """Checks whether a point is contained in the plane"""
        x, y = point
        return 0 <= x < self._size_x and 0 <= y < self._size_y

    def get_point_neighbours(self, point: Point) -> list:
        """Returns valid neighbours for point. Valid ones are those that are contained on the plane"""
        if not self.contain(point):
            raise OutOfPlane(point)

        neighbours = [(self.__add_points(point, rule)) for rule in self._moving_rules.keys()]
        valid_neighbours = filter(self.contain, neighbours)
        return list(valid_neighbours)

    def distance(self, first: Point, second: Point) -> Union[int, float]:
        """Returns distance between 2 point depending on the specified geometry"""
        if not self.contain(first):
            raise OutOfPlane(first)

        if not self.contain(second):
            raise OutOfPlane(second)
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

    def __move_direction(self, from_p: Point, to_p: Point) -> Point:
        """Returns the direction of movement for moving from one point to another"""
        move_direction_raw_value = self.__subtract_points(to_p, from_p)
        try:
            move_direction = self._moving_rules[move_direction_raw_value]
        except KeyError:
            raise ImpossibleMove('Impossible move for current rules: ', from_p, to_p, self._moving_rules)
        return move_direction

    def path_to_commands(self, path: list) -> list:
        """Converts a sequence of points into commands"""
        commands = []
        for i in range(1, len(path)):
            direction = self.__move_direction(path[i - 1], path[i])
            commands.append(direction)
        return commands

    def bfs_path(self, start: Point, end: Point) -> Union[list, None]:
        """Standard Breadth First Search algorithm. Returns path from one point to another"""
        queue = deque()
        queue.append(start)
        explored = set()
        paths_map = {start: None}
        while queue:
            cur_vertex = queue.popleft()
            if cur_vertex == end:
                path = deque()
                path.appendleft(cur_vertex)
                prev_vertex = paths_map[cur_vertex]
                while prev_vertex is not None:
                    path.appendleft(prev_vertex)
                    prev_vertex = paths_map[prev_vertex]
                return list(path)
            else:
                for neighbour in self.get_point_neighbours(cur_vertex):
                    if neighbour not in explored and neighbour not in queue:
                        queue.append(neighbour)
                        paths_map[neighbour] = cur_vertex
                explored.add(cur_vertex)
        return None


if __name__ == '__main__':
    pass
