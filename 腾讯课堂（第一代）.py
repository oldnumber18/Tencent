import time
import pyautogui
from PIL import ImageGrab, Image
import schedule
print("开始运行")

def sao():#该函数主要用 pyautogui 进行 图片扫描 获取坐标 点击
    please = pyautogui.locateOnScreen(photo,grayscale=True,confidence=.9)#识别   photo   图并赋予值给  please
    if please == None: #如果  dian  没有东西
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),n,a,'没有内容')
        #print('点击时间',n,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        time.sleep(2)
    else:#如果 有
        x,y,width,height = please#获取坐标
        pyautogui.click(x,y,button="left")# 得到坐标，点击左键
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),n,a,'已经点击')
        fo = 2
        time.sleep(2)

while True:
    n = b = 0
    photo = Image.open("jia.png");a = '加入会议';n = n + 1;sao()#导入图片：加入会议
    photo = Image.open("list.png");a = '打开列表';n = n + 1;sao()#导入图片：历史会议
    photo = Image.open("class.png");a = '点击班级';n = n + 1;sao()#导入图片：历史会议的号码
    photo = Image.open("take.png");a = '加入会议';n = n +1;sao()#导入图片：加入会议
    pyautogui.typewrite("1115")#输入密码
    photo = Image.open("take2.png");a = '加入会议 no2';n = n + 1;sao()#导入图片：二次确认加入会议   进入界面！！
    print('---------------进入新界面,停止30秒----------------');time.sleep(30)

    photo = Image.open("exit.png")#导入图片：离开会议
    please = pyautogui.locateOnScreen(photo,grayscale=True,confidence=.9)
    if please == None:#m没获取到，证明： 老师在上课
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'开始上课！！！！！！！！！！！！')
        photo = Image.open("qiandao.png")#;a = '签到';n = 0;sao()#导入图片：打开应用
        while True:
            photo = Image.open('jia.png')#导入  加入会议 图片
            please = pyautogui.locateOnScreen(photo,grayscale=True,confidence=.9)
            if please == None:#如果没有 则还在上课
                pass
            else:#如果监测到了，证明不在会议
                print("检测到 ‘加入会议’ 证明其界面没有出现 将取消自动退出 上课 状态")
                break
            please = pyautogui.locateOnScreen(photo,grayscale=True,confidence=.9);print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'已开启 自动签到, 每五秒检测签到一次')
            if please == None :
                pass
            else:
                x,y,width,height = please#获取坐标
                pyautogui.click(x,y,button="left")# 得到坐标，点击左键
                time.sleep(6)
                photo = Image.open("qiandao1.png");a = '签到';n = 0;sao()#导入图片：签到 
                print('已签到');time.sleep(2)
                photo = Image.open("qiandao3.png");a = '签到exit';n = 0;sao()#导入图片：退出签到
            
            time.sleep(5)
        print('------------------------------------')
    else: #已经获取到 离开会议 证明 老师还没开会议
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'没有上课！！！')
        x,y,width,height = please#获取坐标
        pyautogui.click(x,y,button="left")# 得到坐标，点击左键
        photo = Image.open("exit2.png");a = '确认退出2';n=n+1;sao()
        print("十秒钟后继续");time.sleep(10)
        print("---------------------------------------------")
