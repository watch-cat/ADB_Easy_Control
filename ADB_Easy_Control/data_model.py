class Point(object):
    def __init__(self, position_x: int, position_y: int):
        self.position_x = position_x
        self.position_y = position_y


class RectangleArea(object):
    def __init__(self, beginarea_x: int, finisharea_x: int, beginarea_y: int, finisharea_y: int):
        self.beginarea_x = beginarea_x
        self.finisharea_x = finisharea_x
        self.beginarea_y = beginarea_y
        self.finisharea_y = finisharea_y
