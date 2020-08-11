import pyautogui
import keyboard
import time
import random

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



GetPosKey = 'ctrl+alt'          # 选点快捷键
x_lv = y_lv = 0                 # 生产类型坐标,选在普通水处
x_safe = y_safe = 0             # 安全区坐标,建议选在屏幕四周的河流中
total = 19                      # 建筑总数目
buildingType = '水井'
waitingTime = 180               # 生产1份需要的时间
myBuilding = []

class Building:
    def __init__(self,index):
        self.x = self.y = self.level = 0
        self.index = index
        self.name = buildingType

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        print(str(self.index) + '号'+self.name+'中心坐标:x=' + str(self.x) + ',y=' + str(self.y))

    def produce_start(self):
        x1 = self.x + (random.random()-0.5) * 1
        y1 = self.y + (random.random()-0.5) * 1
        level = self.level
        x2 = x_lv + (random.random()-0.5) * 1
        y2 = y_lv + (random.random()-0.5) * 1
        sleeptime = 0.5 + random.random() * 0.3

        check()
        pyautogui.click(x1,y1)
        time.sleep(sleeptime)

        check()
        pyautogui.doubleClick(x=x2, y=y2, interval=sleeptime)
        time.sleep(sleeptime)
        click_safety_area()
        print(str(self.index)+ '号'+self.name+"开始生产,等级:"+str(level))


def click_safety_area():
    pyautogui.click(x_safe + random.random() * 2, y_safe - random.random() * 2)
    time.sleep(0.1 + random.random() * 0.3)
    pyautogui.click(x_safe + random.random() * 2, y_safe - random.random() * 2)
    time.sleep(0.1 + random.random() * 0.3)
    pyautogui.click(x_safe + random.random() * 2, y_safe - random.random() * 2)
    time.sleep(0.1 + random.random() * 0.3)
    pyautogui.click(x_safe + random.random() * 2, y_safe - random.random() * 2)
    time.sleep(0.1 + random.random() * 0.3)

def check():
    if keyboard.is_pressed('esc'):
        input('等待中,输入任意字符恢复执行')
        input('确认恢复?输入任意字符恢复执行')




def init():
    method = int(input('\n>>输入命令:\n0:插件介绍\n1:修改参数\n'
                   '2:初始化坐标\n3:开始挂机\n9:退出程序\n请输入:'))
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
        beginScript()
        return 1
    elif method == 9:
        return 0
    else:
        print('皮?')
        return 1


def introduce():
    print("""\n本脚本是手机游戏江南百景图的辅助脚本.开发仅供个人学习使用.禁止其他人的任何不正当行为,所引起的纠纷本人概不负责.
## 如何使用?
0.  本脚本需要一定python基础
1. 请配合电脑端的安卓模拟器使用
2. 在代码最开始设置相关参数 
3. 初次使用需要手动选点
4. 长按ESC键可中止下一次点击
5. 请打开收税的
6. 尽量不要把水井种在神像后面,挡视野很难命中
7. 无法解决v1.2.6的拼图小游戏
8. 实际使用中会出很多问题,我也懒得更新,凑合着玩吧
9. 建议食用方式: 一边挂着刷钱一边看番, 出问题了自己手动调一下
10. 写给游戏开发者: 你这拼图机制aoe无差别攻击,我都提肝帝们气愤""")
    b = input("输入任意键继续...")
    a = int(input(">> 输入命令:\n1. 查看推荐布局(应天府十九井)\n2. 查看推荐布局(苏州府卅九井)\n请输入:"))
    if a==1:
        print('''应天府十九井\nO O O O O\nO X O X O\nO X ■ O O\nO O X O X\nO O O O O''')
    elif a==2:
        print("""O O O O O O O\nO X O O O X O\nO O X X O O O\nO O X ■ X O O \nO O O X O O O\nO X O O O X O\nO O O O O O O""")
    else:
        print('皮?')
        return


def changeArg():
    global total
    total = int(input('请输入建筑总数:'))
    print('[已更新]\t总计'+str(total)+'座'+buildingType)


def initPos():
    # 清空数据
    f = open('./Data.txt', 'w')
    f.write('')
    f.close()
    # 写入数据
    f = open('./Data.txt', 'a')
    print('请将鼠标移动至生产类型(如普通水,上品水)位置后按下"Ctrl+Alt"')
    if keyboard.wait('ctrl+alt') != 0:
        x, y = pyautogui.position()
        writeStr = str(x).rjust(4)+'\t生产类型\t'+str(y).rjust(4) + '\n'
        f.write(writeStr)
        print('数据已捕获')
    print('请将鼠标移动至安全区位置后按下"Ctrl+Alt"')
    if keyboard.wait('ctrl+alt') != 0:
        x, y = pyautogui.position()
        writeStr = str(x).rjust(4) + '\t安全区\t' + str(y).rjust(4) + '\n'
        f.write(writeStr)
        print('数据已捕获')
    for i in range(total):
        print('请将鼠标移动至建筑位置后按下"Ctrl+Alt",重复' + str(total-i) + '次')
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
    global myBuilding, x_lv, y_lv, x_safe, y_safe
    isBadData = 0
    myBuilding = []
    f = open('./Data.txt', 'r')
    # 读取生产类型坐标
    line_str = f.readline()
    if (line_str == ''):
        isBadData = 1
    else:
        x_lv = int(line_str[0:4])
        y_lv = int(line_str[-4:-1])
    # 读取安全区
    line_str = f.readline()
    if (line_str == ''):
        isBadData = 1
    else:
        x_safe = int(line_str[0:4])
        y_safe = int(line_str[-4:-1])
    # 读取建筑坐标
    numlines = 0
    while (True):
        line_str = f.readline()
        # print(line_str)
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
    # 检查坏数
    if numlines != total:
        isBadData = 1
    if isBadData==1:
        print("⚠Data文件损坏,请重新初始化坐标⚠\n")
        return
    print("脚本加载完毕,开始执行\n")

def real_beginScript():
    print("*********开始挂机*********")
    global myBuilding
    produce_times = 1
    while(True):
        click_safety_area()
        print('> 开始第'+str(produce_times)+'轮生产')
        check()
        for i in range(total):
            myBuilding[i].produce_start()
        print('> 等待成熟')
        time.sleep(waitingTime-total*1.5+random.random()*15)
        print('> 第'+str(produce_times)+'轮生产完毕')
        click_safety_area()
        print('> 20秒后开始下一轮')
        time.sleep(20)
        produce_times += 1


#     print('请将鼠标移动至"普通水"位置后按下"Ctrl+Alt",重复'+str(1)+'次')
#     if keyboard.wait('ctrl+alt') != 0:
#         x_lv, y_lv = pyautogui.position()
#     print('普通水坐标:x=' + str(x_lv) + ',y=' + str(y_lv))
# print('请将鼠标移动至水井中心十字位置后按下"Ctrl+Alt",重复'+str(20)+'次')
# myWell = []
# for i in range(18):
#     myWell.append(Well())
#     myWell[i].set_pos(i)
#
#
# print("*********开始挂机*********")
# while(True):
#     print('***********生产中***********')
#     check()
#     for i in range(18):
#         myWell[i].produce_start(x_lv[0+50*(random.random()-0.5), y_lv[0+50*(random.random()-0.5),i)
#     print('***********等待中***********')
#     time.sleep(200+random.random()*15)
#     print('***********收割中***********')
    # for i in range(20):
    #     myWell[i].produce_end(i)

if __name__ == '__main__':
    print("*****江南百井图刷金币脚本*****")
    Flag = True
    while(Flag):
        Flag=init()