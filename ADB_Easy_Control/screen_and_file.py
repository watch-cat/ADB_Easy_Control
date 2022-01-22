import os
import datetime
from ADB_Easy_Control import device_assistant


def screen_capture() -> str:
    now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    os.system("adb" + device_assistant.multi_devices_helper() + " shell screencap -p /sdcard/screencap.png")
    if not os.path.exists(format(os.getcwd()) + "/ScreenCapture"):
        os.mkdir(format(os.getcwd()) + "/ScreenCapture/")
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " pull /sdcard/screencap.png" + " " + format(
            os.getcwd()) + "/ScreenCapture/" + format(now_time) + ".png")

    return format(now_time) + ".png"


def custompath_screen_capture(filename: str, path: str) -> str:
    os.system("adb" + device_assistant.multi_devices_helper() + " shell screencap -p /sdcard/screencap.png")
    os.system("adb" + device_assistant.multi_devices_helper() + " pull /sdcard/screencap.png" + " " + format(
        path) + "/ScreenCapture/" + format(filename) + ".png")

    return format(filename) + ".png"


def screen_record(time_limit: float) -> str:
    now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    os.system("adb" + device_assistant.multi_devices_helper() + " shell screenrecord --time-limit " + format(
        time_limit) + " /sdcard/screenrecord.mp4")
    if not os.path.exists(format(os.getcwd()) + "/ScreenRecord"):
        os.mkdir(format(os.getcwd()) + "/ScreenRecord/")
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " pull /sdcard/screenrecord.mp4" + " " + format(
            os.getcwd()) + "/ScreenRecord/" + format(now_time) + ".mp4")

    return format(now_time) + ".mp4"


def custompath_screen_record(time_limit: float, filename: str, path: str) -> str:
    os.system("adb" + device_assistant.multi_devices_helper() + " shell screenrecord --time-limit " + format(
        time_limit) + " /sdcard/screenrecord.mp4")
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " pull /sdcard/screenrecord.mp4" + " " + format(
            path) + "/ScreenRecord/" + format(filename) + ".mp4")

    return format(filename) + ".mp4"


def custom_screen_record(time_limit: float, size: str, bit_rate: int, filename: str, path: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell screenrecord --time-limit " + format(
        time_limit) + " --size " + format(size) + " --bit-rate " + format(bit_rate) + " /sdcard/screenrecord.mp4")
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " pull /sdcard/screenrecord.mp4" + " " + format(
            path) + "/ScreenRecord/" + format(filename) + ".mp4")

    return format(filename) + ".mp4"


def pull_file_to_computer(droid_path: str, computer_path: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " pull " + droid_path + " " + computer_path)


def push_file_to_droid(computer_path: str, droid_path: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " push " + computer_path + " " + droid_path)
