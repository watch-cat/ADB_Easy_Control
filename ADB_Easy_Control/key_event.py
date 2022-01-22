import os
from ADB_Easy_Control import device_assistant


# 仅可输入英文字符
def input_text(text: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input text " + format(text))


def input_by_keycode(keycode: int):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent " + format(keycode))


def home_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 3")


def back_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 4")


def volume_up():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 24")


def volume_down():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 25")


def power_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 26")


def space_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 62")


def tab_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 61")


def enter_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 66")


def backspace_delete_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 67")


def escape_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 111")


def forward_delete_button():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 112")


def screen_off():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 223")


def screen_on():
    os.system("adb" + device_assistant.multi_devices_helper() + " shell input keyevent 224")
