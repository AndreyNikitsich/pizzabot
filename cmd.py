import argparse
import re

FIELD_SIZE_2D_RE = re.compile(r'(\d+)[xX](\d+)')
POINT_2D_RE = re.compile(r'\((\d+)\,(\d+)\)')


def field_size(string: str) -> tuple[int, int]:
    match_obj = re.match(FIELD_SIZE_2D_RE, string)
    if match_obj is not None:
        size_x, size_y = int(match_obj.group(1)), int(match_obj.group(2))
        return size_x, size_y
    else:
        raise TypeError()


def point(string: str) -> tuple[int, int]:
    match_obj = re.match(POINT_2D_RE, string)
    if match_obj is not None:
        x, y = int(match_obj.group(1)), int(match_obj.group(2))
        return x, y
    else:
        raise TypeError()


parser = argparse.ArgumentParser(description='Pizzabot program')
parser.add_argument('field_size', type=field_size, help='A string which represents field size looks like \'5x5\'')
parser.add_argument('points', type=point, nargs='+', help='List of delivery points. E.x. (0,1) (0,2) ...')

if __name__ == '__main__':
    pass
