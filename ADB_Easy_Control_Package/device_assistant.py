import os


def get_dpi() -> str:
    dpi_string = os.popen("adb" + multi_devices_helper() + " shell wm density").read().split(" ")[2][:-1]
    return dpi_string


def get_size() -> str:
    size_string = os.popen("adb" + multi_devices_helper() + " shell wm size").read().split(" ")[2][:-1]
    return size_string


def get_size_x() -> str:
    size_x_string = os.popen("adb" + multi_devices_helper() + " shell wm size").read().split(" ")[2][:-1].split("x")[0]
    return size_x_string


def get_size_y() -> str:
    size_y_string = os.popen("adb" + multi_devices_helper() + " shell wm size").read().split(" ")[2][:-1].split("x")[1]
    return size_y_string


def reboot():
    os.system("adb" + multi_devices_helper() + " shell reboot")


def shutdown():
    os.system("adb" + multi_devices_helper() + " shell reboot -p")


def turn_on_wifi():
    os.system("adb" + multi_devices_helper() + " shell svc wifi enable")


def turn_off_wifi():
    os.system("adb" + multi_devices_helper() + " shell svc wifi disable")


def wifi_prefer():
    os.system("adb" + multi_devices_helper() + " shell svc wifi prefer")


def turn_on_data():
    os.system("adb" + multi_devices_helper() + " shell svc data enable")


def turn_off_data():
    os.system("adb" + multi_devices_helper() + " shell svc data disable")


def data_prefer():
    os.system("adb" + multi_devices_helper() + " shell svc data prefer")


def power_stay_on(mode: str):
    os.system("adb" + multi_devices_helper() + " shell svc power stayon " + format(mode))


def kill_adb_server():
    os.system("adb kill-server")


def start_adb_server():
    os.system("adb start_server")


def get_connected_devices() -> list:
    devices_info = os.popen("adb devices -l").read().split()[4:]
    devices_list = []
    for i in range(0, len(devices_info), 7):
        devices_list.append(devices_info[i])
    return devices_list


def get_connected_device_info() -> list:
    devices_info = os.popen("adb devices -l").read().split()[4:]
    return devices_info


is_multi_devices = 0
current_device = ""


def multi_devices_helper() -> str:
    if is_multi_devices == 1 and not current_device == "":
        return format(" -s " + current_device)
    else:
        return ""
