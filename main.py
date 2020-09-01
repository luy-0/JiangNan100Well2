import pyautogui
import keyboard
import time
import random

import flow_ctrl as flow
import data_ctrl as data

'''
写在前面

0.  本脚本需要一定python基础
1.  本脚本需要配合电脑模拟器使用
2.  本脚本无法破解v1.2.6版本更新的拼图小游戏
3.  纯基于模拟点击,无图像识别功能, 因此可能存在以下问题:
3.1 在触摸点浮动时误触其他图像导致工作错误
3.2 点击时正好有土行孙/补天石小贩/西域商人/居民对话经过导致工作失败
3.3 由于模拟器触摸不灵敏导致点击遗漏
4.  在非等待态的情况下,长按ESC键可以强行终止下一次点击
5.  在非等待态的情况下,将鼠标移至桌面的四个角落之一可强行终止程序
6.  本脚本仅用于学习交流,禁止用于商业用途(虽然写的这么烂谁会用来商业用途),否则引起的相关责任与开发者无关
7.  我曾在极端愤怒的情况下一晚上写完了这个脚本
'''



GetPosKey = 'ctrl+alt'                          # 选点快捷键
total = data.total                              # 建筑总数目
is_tax_station_work = data.is_tax_station_work  # 税课司工作否
buildingType = data.buildingType                # 生产类型(名称)
pro_type_level = data.pro_type_level            # 生产等级
pro_manager = data.pro_manager                  # 生产者
waitingTime = data.waitingTime                  # 生产1份需要的时间
myBuilding = []


class Building:
    def __init__(self, index):
        self.x = self.y = 0
        self.level = pro_type_level
        self.index = index
        self.name = buildingType

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        print(str(self.index) + '号'+self.name+'中心坐标:x=' + str(self.x) + ',y=' + str(self.y))

    def click_pro_type(self):
        flow.short_sleep(0.2)
        flow.click(data.pro_type[self.level][0], data.pro_type[self.level][1])
        flow.short_sleep(0.8)

    def click_pro_manager(self):
        flow.click(data.pro_manager_pos[pro_manager][0], data.pro_manager_pos[pro_manager][1])

    def produce_once(self):
        flow.click_safe()
        flow.click(self.x, self.y)
        self.click_pro_type()
        self.click_pro_manager()
        flow.click_safe()
        flow.drag_safe()

    def produce_end(self):
        flow.click_safe()
        flow.click(self.x, self.y)
        flow.click_safe()

    # def produce_start(self):
    #     x1 = self.x + (random.random()-0.5) * 1
    #     y1 = self.y + (random.random()-0.5) * 1
    #     level = self.level
    #     x2 = x_lv + (random.random()-0.5) * 1
    #     y2 = y_lv + (random.random()-0.5) * 1
    #     sleeptime = 0.5 + random.random() * 0.3
    #
    #     flow.check()
    #     pyautogui.click(x1,y1)
    #     time.sleep(sleeptime)
    #
    #     flow.check()
    #     pyautogui.doubleClick(x=x2, y=y2, interval=sleeptime)
    #     time.sleep(sleeptime)
    #     flow.click_safe()
        # self.print_begin_pro()

    # def print_begin_pro(self):
    #     print(str(self.index) + '号' + self.name + "开始生产,等级:" + str(self.level))
    #
    # def print_end_pro(self):
    #     print(str(self.index) + '号' + self.name + "结束生产,等级:" + str(self.level))



def init():
    method = int(input('\n>>输入命令:\n0:插件介绍\n1:修改参数\n'
                   '2:初始化坐标\n3.初始化视角(画室)\n4:开始挂机\n9:退出程序\n请输入:'))
    if method == 0:
        introduce()
        return 1
    elif method == 1:
        changeArg()
        return 1
    elif method == 2:
        initPos()
        return 1
    elif method == 3:
        flow.goto_painting_room()
        return 1
    elif method == 4:
        beginScript()
        return 1
    elif method == 9:
        return 0
    elif method == 666:
        flow.check_hwnd()
        flow.goto_painting_room()
        beginScript()
    else:
        print('皮?')
        return 1


def introduce():
    print("本脚本仅供个人学习代码使用.请勿用于实际游戏!!\n"
          "请配合电脑端的安卓模拟器(推荐使用逍遥)\n"
          "无法解决拼图小游戏, 但是已经尽可能地规避了\n"
          "如果你只能刷一轮是正常的.请自己阅读源代码并修改\n"
          "长按ESC或将鼠标移动至屏幕四角可以强行阻止下一次点击\n"
          )
    b = input("输入任意键返回")
    return


def changeArg():
    global total, buildingType, waitingTime, is_tax_station_work, pro_manager, pro_type_level
    total = int(input('请输入建筑总数:'))
    buildingType = input('请输入建筑名称:')
    waitingTime = int(input('请输入单次生产时长(分钟):'))
    pro_type_level = int(input("请输入生产等级(1/2/3/4):")) - 1
    is_tax_station_work = bool(input("税课司是否工作?工作输入1,反之输入0:"))
    pro_manager = int(input("是否派遣特殊居民?派遣输入1,反之输入0:"))



def initPos():
    # 清空数据
    f = open('./Data.txt', 'w')
    f.write('')
    f.close()
    # 写入数据
    f = open('./Data.txt', 'a')
    for i in range(total):
        print('请将鼠标移动至建筑位置后按下'+GetPosKey+',重复' + str(total-i) + '次')
        if keyboard.wait('ctrl+alt') != 0:
            x, y = pyautogui.position()
            writeStr = str(x).rjust(4) + '\t'+buildingType+'\t' + str(y).rjust(4) + '\n'
            f.write(writeStr)
            print('数据已捕获')
    f.close()
    print('坐标初始化完毕\n')


def beginScript():
    initBuilding()
    real_beginScript()


def initBuilding():
    global myBuilding
    myBuilding = []
    f = open('./Data.txt', 'r')
    numlines = 0
    while (True):
        line_str = f.readline()
        if (line_str == ''):
            break
        else:
            x = int(line_str[0:4])
            y = int(line_str[-4:-1])
            newBuilding = Building(numlines)
            myBuilding.append(newBuilding)
            myBuilding[numlines].set_pos(x,y)
            numlines += 1
    f.close()
    print("脚本加载完毕,开始执行\n")


def real_beginScript():
    print("****开始挂机****")
    global myBuilding
    produce_times = 1
    flow.window_max()
    flow.click_safe()
    while(True):
        flow.window_max()
        flow.click_safe()
        print('> 开始第'+str(produce_times)+'轮生产\n本次生产等级为'+str(pro_type_level+1))
        if(pro_manager):
            print("使用角色生产")
        else:
            print("不使用角色生产")
        flow.check()

        for i in range(total):
            myBuilding[i].produce_once()

        if (produce_times%10) == 0:
            flow.map_y2y()
            flow.goto_painting_room()

        flow.wait_pro_over()

        if is_tax_station_work != 1:
            for i in range(total-1, -1, -1):
                myBuilding[i].produce_end()

        print('> 第'+str(produce_times)+'轮生产完毕')
        flow.click_safe()
        produce_times += 1


if __name__ == '__main__':
    print("***江南百井图刷金币脚本***")
    Flag = True
    while(Flag):
        Flag=init()