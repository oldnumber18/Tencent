import time
import pyautogui
from PIL import ImageGrab, Image

print("开始运行")

def ding():
    b = pyautogui.locateOnScreen(a,grayscale=True,confidence=.9)#截取屏幕当前界面并且查看是否有目标地方
    if b==None:
        print("暂无识别内容")
    else:
        x,y,width,height=b
        time.sleep(2)
        pyautogui.click(x,y,button="left")
        print("点击成功")
        time.sleep(6)

while True:
    if True:
        a=Image.open("1.png")#调去需要点击的图片
        ding()
    if True:
        a=Image.open("2.png")
        ding()
    if True:
        a=Image.open("3.png")
        ding()