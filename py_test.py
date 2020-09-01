import win32gui
import win32api
import win32con
import time
import pyautogui
import keyboard

hwnd_title = {}


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def all_hwnds():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t :
            print (h, t)

def use_win32gui_max_min():
    all_hwnds()
    hwnd = int(input('\n请输入句柄:'))
    print('句柄已获得:' + win32gui.GetWindowText(hwnd))
    time.sleep(1)
    win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0)
    time.sleep(1)
    win32gui.PostMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)


def Beep():
    # 发出蜂鸣声
    # Beep(freq, dur)
    # freq : int
    # dur : int   (微秒)
    for i in range(3):
        win32api.Beep(2000,300)
        time.sleep(0.1)
    for i in range(3):
        win32api.Beep(3000,100)
        time.sleep(0.1)
    win32api.Beep(1000,1000)




if __name__ == '__main__':
    pass