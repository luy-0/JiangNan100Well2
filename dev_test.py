import pyautogui
import keyboard
import flow_ctrl as flow
import random
import time

point_num = 0


def init():
    # todo 从文件中读取数据
    pass


def get_pos():
    # todo 选点
    # 写入数据文件,编号
    # 清除数据文件
    if keyboard.wait('ctrl+alt') != 0:
        x, y = pyautogui.position()
        writeStr = str(x).rjust(4)+'\t生产类型\t'+str(y).rjust(4) + '\n'
        print(writeStr)


def moveto(x,y):
    # todo 移动到指定位置
    pyautogui.moveTo(x, y, 0.5)


def range_test(x,y,r):
    # todo 测试选点范围有多大
    pass


def check_esc():
    # todo 测试是否按下esc,返回0/1
    pass


def test_import():
    print('import success!')


def be_hooked(event):
    print('hook!')
    return 666


if __name__ == '__main__':
    # init()
    # moveto(765,260)
    # while True:
    # b = -50
    # flow.short_sleep(2)
    #     get_pos()
    # flow.be_smaller()
    # flow.click_safe()
    # flow.map_2_yingtian()
    # flow.goto_painting_room()
    # flow.drag_down()
    # flow.drag_safe()
    while True:
        get_pos()
    # flow.map_y2y()
    # flow.goto_painting_room()
        # flow.click_safe()
        # flow.drag_down(5)
        # flow.drag_up(5)
    # flow.drag_test()
    # flow.short_sleep(10)
    # pyautogui.moveTo(900, 500)
    # flow.click(900,500)
    # flow.drag_right(10)
    # flow.drag_down(10)
    # flow.be_smaller()
    # flow.goto_painting_room()
    # pyautogui.moveTo(900, 500)
    # a = 10%10
    # print(a)
    # flow.map_2_suzhou()
    # flow.map_2_yingtian()


