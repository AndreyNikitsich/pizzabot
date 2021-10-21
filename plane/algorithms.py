from collections import deque
from typing import Union
from .plane import Plane, OutOfPlane, Point


def bfs_path(plane: Plane, start: Point, end: Point) -> Union[list, None]:
    """Returns path from one point to another."""

    if not plane.contains(start):
        raise OutOfPlane(start)

    if not plane.contains(end):
        raise OutOfPlane(end)

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
            for neighbour in plane.get_neighbours_point(cur_vertex):
                if neighbour not in explored and neighbour not in queue:
                    queue.append(neighbour)
                    paths_map[neighbour] = cur_vertex
            explored.add(cur_vertex)
    return None
