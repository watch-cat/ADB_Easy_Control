from ADB_Easy_Control import touch_event
from ADB_Easy_Control import data_model


def point_touch_withobj(position: data_model.Point, sleep_time: float):
    touch_event.point_touch(position.position_x, position.position_y, sleep_time)


def point_swipe_withobj(start_position: data_model.Point, end_position: data_model.Point, swipe_time: float,
                        sleep_time: float):
    touch_event.point_swipe(start_position.position_x, start_position.position_y, end_position.position_x,
                            end_position.position_y, swipe_time, sleep_time)


def point_longtime_touch_withobj(position: data_model.Point, touch_time: float, sleep_time: float):
    touch_event.point_longtime_touch(position.position_x, position.position_y, touch_time, sleep_time)


def rectangle_area_touch_withobj(area: data_model.RectangleArea, sleep_time: float):
    touch_event.rectangle_area_touch(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                                     sleep_time)


def rectangle_area_longtime_touch_withobj(area: data_model.RectangleArea, touch_time: float, sleep_time: float):
    touch_event.rectangle_area_longtime_touch(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                                              touch_time, sleep_time)


def rectangle_area_swipe_withobj(start_area: data_model.RectangleArea, end_area: data_model.RectangleArea,
                                 swipe_time: float,
                                 sleep_time: float):
    touch_event.rectangle_area_swipe(start_area.beginarea_x, start_area.finisharea_x, start_area.beginarea_y,
                                     start_area.finisharea_y, end_area.beginarea_x, end_area.finisharea_x,
                                     end_area.beginarea_y, end_area.finisharea_y, swipe_time, sleep_time)


def rectangle_inarea_rand_swipe_withobj(area: data_model.RectangleArea, min_swipe_distance: int,
                                        max_swipe_distance: int,
                                        swipe_time: float, sleep_time: float):
    touch_event.rectangle_inarea_rand_swipe(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                                            min_swipe_distance, max_swipe_distance, swipe_time, sleep_time)
