class ImpossibleMove(Exception):
    """Rises when try to make a move that is not allowed by the rules."""

    def __init__(self, message):
        super().__init__(message)


class OutOfPlane(Exception):
    """Rises when something is done with a point that is outside the plane."""

    def __init__(self, point, plane):
        message = f'Point {point} is outside the {plane}'
        super().__init__(message)


class WrongGeometry(Exception):
    """Rises when wrong wrong geometry is used."""

    def __init__(self, message):
        super().__init__(message)
