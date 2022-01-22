import os
from ADB_Easy_Control import device_assistant


def get_grep_or_findstr() -> str:
    if os.name == "nt":
        return "findstr"
    else:
        return "grep"


def get_current_activity() -> str:
    package_and_activity_string = os.popen(
        "adb" + device_assistant.multi_devices_helper() + " shell dumpsys activity activities | " + get_grep_or_findstr() + " mCurrentFocus").read().split(
        " ")[4]
    separator = "/"
    activity_string = package_and_activity_string[package_and_activity_string.index(separator) + 1:-2]
    return activity_string


def get_current_package() -> str:
    package_and_activity_string = os.popen(
        "adb" + device_assistant.multi_devices_helper() + " shell dumpsys activity activities | " + get_grep_or_findstr() + " mCurrentFocus").read().split(
        " ")[4]
    separator = "/"
    package_string = package_and_activity_string[:package_and_activity_string.index(separator)]
    return package_string


def start_activity(target_package: str, target_activity: str):
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " shell am start -n " + target_package + "/" + target_activity)


def start_activity_with_parameter(target_package: str, target_activity: str, parameter: str):
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " shell am start -n " + target_package + "/" + target_activity + " -d " + parameter)


def start_activity_by_action(target_intent_action: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell am start -a " + target_intent_action)


def start_activity_by_action_parameter(target_intent_action: str, parameter: str):
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " shell am start -a " + target_intent_action + " -d " + parameter)


def start_service(target_package: str, target_service: str):
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " shell am startservice -n " + target_package + "/" + target_service)


def start_service_with_parameter(target_package: str, target_service: str, parameter: str):
    os.system(
        "adb" + device_assistant.multi_devices_helper() + " shell am start -n " + target_package + "/" + target_service + " -d " + parameter)


def send_broadcast(parameter_and_action: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell am broadcast " + parameter_and_action)


def stop_app(target_package: str):
    os.system("adb" + device_assistant.multi_devices_helper() + " shell am force-stop " + target_package)
