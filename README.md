# JiangNan100Well2
江南百景图_水井刷铜币脚本

## 写在前面

0. 本脚本需要一定python基础
1. 本脚本需要配合电脑模拟器使用
2. 本脚本无法破解v1.2.6版本更新的拼图小游
3. 纯基于模拟点击,无图像识别功能, 因此可能存在以下问题:
   1. 在触摸点浮动时误触其他图像导致工作错误
   2. 点击时正好有土行孙/补天石小贩/西域商人/居民对话经过导致工作失败
   3. 由于模拟器触摸不灵敏导致点击遗漏
4. 在非等待态的情况下,长按ESC键可以强行终止下一次点击
5.  在非等待态的情况下,将鼠标移至桌面的四个角落之一可强行终止程序
6. 本脚本仅用于学习交流,禁止用于商业用途(虽然写的这么烂谁会用来商业用途),否则引起的相关责任与开发者无关
7. 我曾在极端愤怒的情况下一晚上写完了这个脚本

## 用到的库

1. PyAutoGui 

   这是一个使用python模拟鼠标操作的开源库. 简单易用.

   安装

   ```
   pip install pyautogui
   ```

   [🔗文档链接](https://pyautogui.readthedocs.io/en/latest/)

   [🔗GitHub仓库](https://github.com/asweigart/pyautogui)

2. keyboard

   这是一个使用python模拟键盘操作的开源库, API较多

   安装

   ```
   pip install keyboard
   ```

   [🔗文档与仓库](https://github.com/boppreh/keyboard)