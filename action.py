from pyautogui import ImageNotFoundException
import pyautogui
import time
import keyboard

base_url = ".\\img\\"
screen_tole = 1
cur_img = ""


def center(location):
    center_x = (location[0] + location[2] // 2) // screen_tole
    center_y = (location[1] + location[3] // 2) // screen_tole
    return center_x, center_y


def get_x_y(img_name):
    global cur_img
    cur_img = image_path = f"{base_url}{img_name}"
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.9)
    except ImageNotFoundException:
        return None
    # location是一个元组：(left, top, width, height)
    return center(location)


def click(center):
    global cur_img
    if center == None:
        print(f"没找到图片{cur_img}捏～")
        return False
    x, y = center
    pyautogui.click(x, y)
    return True


def double_click(center):
    global cur_img
    if center == None:
        print(f"没找到图片{cur_img}捏～")
        return False
    x, y = center
    pyautogui.doubleClick(x, y)
    return True


def right_click(center):
    global cur_img
    if center == None:
        print(f"没找到图片{cur_img}捏～")
        return False
    x, y = center
    pyautogui.rightClick(x, y)
    return True


def do_type(type, message):
    if type == 1:
        return click(get_x_y(message))
    elif type == 2:
        return double_click(get_x_y(message))
    elif type == 3:
        return right_click(get_x_y(message))
    elif type == 4:
        pyautogui.scroll(message)
        return True
    elif type == 5:
        time.sleep(message)
        return True
    elif type == 6:
        keyboard.write(message)
        return True
    elif type == 7:
        pyautogui.press(message)
        return True
    elif type == 8:
        pyautogui.hotkey(*message)
        return True
    else:
        print(f"类型{type}不存在")
        return False


def do_cycle_type(type, num, message):
    if num == -1:
        # 无限循环
        while True:
            if do_type(type, message) == False:
                break
            time.sleep(0.1)
    else:
        # 指定次数的循环
        for i in range(num):
            if do_type(type, message) == False:
                break
            time.sleep(0.1)
