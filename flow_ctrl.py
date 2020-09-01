import pyautogui
import keyboard
import win32gui
import win32api
import win32con
import random
import time
import data_ctrl as data

bias_max = data.bias_max      # 最大偏移像素
drag_distance = data.drag_distance # 拖拽距离
safe_point_x = data.safe_point_x
safe_point_y = data.safe_point_y        # 安全区
cachet_x = data.cachet_xy[0]
cachet_y = data.cachet_xy[1]# 府印
ground_sill_x = data.ground_sill_xy[0]
ground_sill_y = data.ground_sill_xy[1] # 地基
map_choice_x = data.map_choice_xy[0]
map_choice_y = data.map_choice_xy[1]    # 地图选项
city_1_in_map_x = data.city_1_in_map_xy[0]
city_1_in_map_y = data.city_1_in_map_xy[1]  # 应天府在地图上的坐标(未移动过)
city_2_in_map_x = data.city_2_in_map_xy[0]
city_2_in_map_y = data.city_2_in_map_xy[1]   # 苏州府在地图上的坐标(移动过)


hwnd = 0               # 窗口句柄
hwnd_title = {}         # 当前句柄组


def click(x,y):
    bias = (random.random() - 0.5) * 2 * bias_max
    x += bias
    y += bias
    check()
    pyautogui.click(x,y)
    # print('click!')
    short_sleep(0.4)
    check()


# 安全检测
def check():
    if keyboard.is_pressed('esc'):
        a = ''
        while(a != "replay"):
            a = input('确认恢复?输入"replay"恢复执行')


def click_safe():
    for i in range(2):
        click(safe_point_x, safe_point_y)


def drag_safe():
    # 拖拽画面以反检测
    drag_down(1)
    drag_up(1)


# 初始化场景


def goto_painting_room():
    click_safe()
    goto_center()
    be_smaller()
    ground_sill()
    goto_center()
    drag_left(5)
    drag_down(5)
    click_safe()


# 画面控制


def goto_center():
    pyautogui.moveTo(900, 500)

def be_smaller():
    # 视角变高
    short_sleep(2)
    height = -500
    keyboard.press('ctrl')
    short_sleep(1)
    pyautogui.scroll(height)
    short_sleep(1)
    keyboard.release('ctrl')
    short_sleep(1)


def ground_sill():
    click(cachet_x, cachet_y)
    short_sleep(1)
    click(ground_sill_x, ground_sill_y)
    short_sleep(1)
    click(cachet_x, cachet_y)


def map_choice():
    click_safe()
    click_safe()
    click(cachet_x, cachet_y)
    short_sleep(1)
    click(map_choice_x, map_choice_y)
    short_sleep(1)


def drag_left(n):
    for i in range(n):
        check()
        pyautogui.mouseDown()
        short_sleep(0.1)
        pyautogui.move(+50, 0, 0.11)
        pyautogui.mouseUp()
        pyautogui.move(-50, 0)
        short_sleep(0.1)


def drag_right(n):
    for i in range(n):
        check()
        pyautogui.mouseDown()
        short_sleep(0.1)
        pyautogui.move(-50, 0, 0.11)
        pyautogui.mouseUp()
        pyautogui.move(+50, 0)
        short_sleep(0.1)


def drag_up(n):
    for i in range(n):
        check()
        pyautogui.mouseDown()
        short_sleep(0.3)
        pyautogui.move(0, 50, 0.11)
        pyautogui.mouseUp()
        pyautogui.move(0, -50)
        short_sleep(0.3)


def drag_down(n):
    for i in range(n):
        check()
        pyautogui.mouseDown()
        short_sleep(0.3)
        pyautogui.move(0, -50, 0.11)
        pyautogui.mouseUp()
        pyautogui.move(0, 50)
        short_sleep(0.3)


def drag_test_func(event):
    # print('called')
    if keyboard.is_pressed('W'):
        print('W')
        drag_up()
        pyautogui.move(0, -50)
    elif event.event_type == 'S':
        drag_down()
    elif event.name == 'A':
        drag_left()
    elif event.name == 'D':
        drag_right()


def drag_test():
#     flag = True
    keyboard.hook_key('W', drag_test_func, 1)
    keyboard.hook_key('S', drag_test_func)
    keyboard.hook_key('A', drag_test_func)
    keyboard.hook_key('D', drag_test_func)
#     a = input('输入任意')


def map_2_suzhou():
    click_safe()
    map_choice()
    goto_center()
    drag_down(10)
    drag_right(10)
    click(city_2_in_map_x, city_2_in_map_y)
    short_sleep(10)
    click_safe()
    print('> 当前切换至苏州府')


def map_2_yingtian():
    click_safe()
    map_choice()
    click(city_1_in_map_x, city_1_in_map_y)
    short_sleep(10)
    click_safe()
    print('> 当前切换至应天府')


def map_y2y():
    map_2_suzhou()
    map_2_yingtian()


# 获取句柄
def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def all_hwnds():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t :
            print (h, t)


def hwnd_init():
    all_hwnds()
    global hwnd
    hwnd = int(input('\n请输入句柄:'))
    print('句柄已获得:' + win32gui.GetWindowText(hwnd))


def check_hwnd():
    if hwnd == 0:
        hwnd_init()


# 窗口最大化,最小化
def window_max():
    check_hwnd()
    win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0)
    short_sleep(1)


def window_min():
    check_hwnd()
    win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
    short_sleep(1)


def window_to_top():
    if hwnd == 0:
        hwnd_init()
        win32gui.SetForegroundWindow(hwnd)
    short_sleep(1)


def beep():
    # 发出蜂鸣声
    for i in range(3):
        win32api.Beep(2000,300)
        time.sleep(0.1)
    for i in range(3):
        win32api.Beep(3000,100)
        time.sleep(0.1)
    win32api.Beep(1000,1000)


# 休眠
def short_sleep(time_sec):
    k = (random.random()-0.5) * 0.6 +1
    # time_sec *= k       # 随机0.7~1.3倍时间
    time.sleep(time_sec)


def long_sleep(time_min):
    # todo 将长时间分解,每十分钟点一次安全区
    window_min()
    for i in range(time_min-1):
        short_sleep(60)
        print('> '+str(time_min-i-1)+'分钟后成熟.')
    short_sleep(60)
    beep()
    window_max()


# 流程
def wait_pro_over():
    print('> 当前时间为'+time.strftime(" %H:%M ", time.localtime()) +
          '\t需等待:'+str(data.waitingTime)+'分钟.')
    window_min()
    long_sleep(data.waitingTime)






if __name__ == '__main__':
    window_to_top()