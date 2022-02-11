import os
import time
import random
import math
from ADB_Easy_Control import data_model, device_assistant
from functools import singledispatch


@singledispatch
def point_touch(position_x: int, position_y: int, sleep_time: float):
    os.system('adb' + device_assistant.multi_devices_helper() + ' shell input tap ' + format(position_x) + ' ' + format(
        position_y))
    time.sleep(sleep_time)


@point_touch.register(data_model.Point)
def _(position: data_model.Point, sleep_time: float):
    point_touch(position.position_x, position.position_y, sleep_time)


@singledispatch
def point_swipe(start_position_x: int, start_position_y: int, end_position_x: int, end_position_y: int,
                swipe_time: float, sleep_time: float):
    if swipe_time == 0:
        os.system('adb' + device_assistant.multi_devices_helper() + ' shell input swipe ' + format(
            start_position_x) + ' ' + format(start_position_y) + ' ' + format(
            end_position_x) + ' ' + format(end_position_y))

    if swipe_time != 0:
        if swipe_time > 5:
            print('You may have entered too long a slide time of ' + format(
                swipe_time) + ' seconds.\nNote that the sliding time is in seconds and not milliseconds.')
        os.system('adb' + device_assistant.multi_devices_helper() + ' shell input swipe ' + format(
            start_position_x) + ' ' + format(start_position_y) + ' ' + format(
            end_position_x) + ' ' + format(end_position_y) + '' + format(swipe_time * 1000))

    time.sleep(sleep_time)


@point_swipe.register(data_model.Point)
def _(start_position: data_model.Point, end_position: data_model.Point, swipe_time: float,
      sleep_time: float):
    point_swipe(start_position.position_x, start_position.position_y, end_position.position_x,
                end_position.position_y, swipe_time, sleep_time)


@singledispatch
def point_longtime_touch(position_x: int, position_y: int, touch_time: float, sleep_time: float):
    if touch_time > 5:
        # print('您可能输入了过长的滑动时间，' + format(touch_time) + '秒\n请注意，滑动时间的单位为秒而非毫秒')
        print('You may have entered too long a touch time of ' + format(
            touch_time) + ' seconds.\nNote that the touching time is in seconds and not milliseconds.')
    os.system(
        'adb' + device_assistant.multi_devices_helper() + ' shell input swipe ' + format(position_x) + ' ' + format(
            position_y) + ' ' + format(
            position_x) + ' ' + format(position_y) + '' + format(touch_time * 1000))

    time.sleep(sleep_time)


@point_longtime_touch.register(data_model.Point)
def _(position: data_model.Point, touch_time: float, sleep_time: float):
    point_longtime_touch(position.position_x, position.position_y, touch_time, sleep_time)


@singledispatch
def rectangle_area_touch(beginarea_x: int, finisharea_x: int, beginarea_y: int, finisharea_y: int, sleep_time: float):
    rand_position_x = random.randint(beginarea_x, finisharea_x)
    rand_position_y = random.randint(beginarea_y, finisharea_y)
    os.system(
        'adb' + device_assistant.multi_devices_helper() + ' shell input tap ' + format(rand_position_x) + ' ' + format(
            rand_position_y))
    time.sleep(sleep_time)


@rectangle_area_touch.register(data_model.RectangleArea)
def _(area: data_model.RectangleArea, sleep_time: float):
    rectangle_area_touch(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                         sleep_time)


@singledispatch
def rectangle_area_longtime_touch(beginarea_x: int, finisharea_x: int, beginarea_y: int, finisharea_y: int,
                                  touch_time: float, sleep_time: float):
    rand_position_x = random.randint(beginarea_x, finisharea_x)
    rand_position_y = random.randint(beginarea_y, finisharea_y)
    os.system(
        'adb' + device_assistant.multi_devices_helper() + ' shell input swipe' + format(rand_position_x) + ' ' + format(
            rand_position_y) + ' ' + format(
            rand_position_x) + ' ' + format(rand_position_y) + '' + format(touch_time * 1000))
    time.sleep(sleep_time)


@rectangle_area_longtime_touch.register(data_model.RectangleArea)
def _(area: data_model.RectangleArea, touch_time: float, sleep_time: float):
    rectangle_area_longtime_touch(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                                  touch_time, sleep_time)


@singledispatch
def rectangle_area_swipe(start_beginarea_x: int, start_finisharea_x: int, start_beginarea_y: int,
                         start_finisharea_y: int, end_beginarea_x: int, end_finisharea_x: int, end_beginarea_y: int,
                         end_finisharea_y: int, swipe_time: float, sleep_time: float):
    rand_start_position_x = random.randint(start_beginarea_x, start_finisharea_x)
    rand_start_position_y = random.randint(start_beginarea_y, start_finisharea_y)
    rand_end_position_x = random.randint(end_beginarea_x, end_finisharea_x)
    rand_end_position_y = random.randint(end_beginarea_y, end_finisharea_y)

    point_swipe(rand_start_position_x, rand_start_position_y, rand_end_position_x, rand_end_position_y, swipe_time,
                sleep_time)


@rectangle_area_swipe.register(data_model.RectangleArea)
def _(start_area: data_model.RectangleArea, end_area: data_model.RectangleArea,
      swipe_time: float,
      sleep_time: float):
    rectangle_area_swipe(start_area.beginarea_x, start_area.finisharea_x, start_area.beginarea_y,
                         start_area.finisharea_y, end_area.beginarea_x, end_area.finisharea_x,
                         end_area.beginarea_y, end_area.finisharea_y, swipe_time, sleep_time)


@singledispatch
def rectangle_inarea_rand_swipe(beginarea_x: int, finisharea_x: int, beginarea_y: int, finisharea_y: int,
                                min_swipe_distance: int, max_swipe_distance: int, swipe_time: float, sleep_time: float):
    if min_swipe_distance > max_swipe_distance:
        print("最小滑动距离" + format(min_swipe_distance) + "大于最大滑动距离" + format(max_swipe_distance))
        return
    diagonal_distance = math.hypot(finisharea_x - beginarea_x, finisharea_y - beginarea_y)
    if max_swipe_distance > diagonal_distance:
        print("设定的最大滑动距离" + format(max_swipe_distance) + "大于区域的对角线距离" + format(diagonal_distance))
        max_swipe_distance = diagonal_distance
        if min_swipe_distance > max_swipe_distance:
            print("设定的最小滑动距离" + format(min_swipe_distance) + "大于区域的对角线距离" + format(diagonal_distance))
            min_swipe_distance = max_swipe_distance

    rand_distance = random.randint(min_swipe_distance, max_swipe_distance)
    rand_degree = random.randint(0, 90)
    x_move_distance = math.cos(math.radians(rand_degree)) * rand_distance
    y_move_distance = math.sin(math.radians(rand_degree)) * rand_distance
    rand_direction = random.randint(1, 4)
    if rand_direction == 1:
        rand_start_position_x = random.randint(beginarea_x, int(finisharea_x - x_move_distance))
        rand_start_position_y = random.randint(beginarea_y, int(finisharea_y - y_move_distance))
        rand_end_position_x = rand_start_position_x + x_move_distance
        rand_end_position_y = rand_start_position_y + y_move_distance
    elif rand_direction == 2:
        rand_start_position_x = random.randint(beginarea_x, int(finisharea_x - x_move_distance))
        rand_start_position_y = random.randint(int(beginarea_y + y_move_distance), finisharea_y)
        rand_end_position_x = rand_start_position_x + x_move_distance
        rand_end_position_y = rand_start_position_y - y_move_distance
    elif rand_direction == 3:
        rand_start_position_x = random.randint(int(beginarea_x + x_move_distance), finisharea_x)
        rand_start_position_y = random.randint(beginarea_y, int(finisharea_y - y_move_distance))
        rand_end_position_x = rand_start_position_x - x_move_distance
        rand_end_position_y = rand_start_position_y + y_move_distance
    else:
        rand_start_position_x = random.randint(int(beginarea_x + x_move_distance), finisharea_x)
        rand_start_position_y = random.randint(int(beginarea_y + y_move_distance), finisharea_y)
        rand_end_position_x = rand_start_position_x - x_move_distance
        rand_end_position_y = rand_start_position_y - y_move_distance

    point_swipe(rand_start_position_x, rand_start_position_y, int(rand_end_position_x), int(rand_end_position_y),
                swipe_time, sleep_time)


@rectangle_inarea_rand_swipe.register(data_model.RectangleArea)
def _(area: data_model.RectangleArea, min_swipe_distance: int, max_swipe_distance: int,
      swipe_time: float, sleep_time: float):
    rectangle_inarea_rand_swipe(area.beginarea_x, area.finisharea_x, area.beginarea_y, area.finisharea_y,
                                min_swipe_distance, max_swipe_distance, swipe_time, sleep_time)
