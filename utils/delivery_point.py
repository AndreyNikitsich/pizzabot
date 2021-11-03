class DeliveryPoint:
    __slots__ = ['point', 'actions']

    def __init__(self, point: tuple[int, int] = (0, 0), actions: list = None):
        if actions is None:
            actions = []
        self.point = point
        self.actions = actions
