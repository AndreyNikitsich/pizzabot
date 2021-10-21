import argparse
import re


class CMDParser:
    FIELD_SIZE_2D_RE = re.compile(r'(\d+)[xX](\d+)')
    POINT_2D_RE = re.compile(r'\((\d+)\,(\d+)\)')

    @classmethod
    def get_parser(cls) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description='Pizzabot program')
        parser.add_argument('field_size', type=cls.__field_size_type,
                            help='A string which represents field size looks like \'5x5\'')
        parser.add_argument('points', type=cls.__point_type, nargs='+',
                            help='List of delivery points. E.x. (0,1) (0,2) ...')
        return parser

    @classmethod
    def __point_type(cls, string: str) -> tuple[int, int]:
        match_obj = re.match(cls.POINT_2D_RE, string)
        if match_obj is not None:
            x, y = int(match_obj.group(1)), int(match_obj.group(2))
            return x, y
        else:
            raise argparse.ArgumentTypeError(f'Invalid point format {string}.')

    @classmethod
    def __field_size_type(cls, string: str) -> tuple[int, int]:
        match_obj = re.match(cls.FIELD_SIZE_2D_RE, string)
        if match_obj is not None:
            size_x, size_y = int(match_obj.group(1)), int(match_obj.group(2))
            return size_x, size_y
        else:
            raise argparse.ArgumentTypeError(f'Invalid field_size format {string}.')
