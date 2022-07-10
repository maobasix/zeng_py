import requests
import datetime
import json
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl  # 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False  # 设置正常显示符号

Data = {}


class Request_Data:  # 数据收集类
    def __init__(self, url, Time):
        self.Time = Time
        self.url = url

    def Get_Info(self):  # 收集函数
        try:
            datetime.datetime.strptime(self.Time, '%Y-%m-%d')
        except ValueError:
            Data['type'] = 'False'
            Data['msg'] = '时间格式错误'
            json_Data = json.dumps(Data)
            return json_Data
        Form_Data = {
            'key': 'd334721cf6eba2d619a5855420ec352c',
            'date': self.Time
        }
        try:
            resp = requests.post(self.url, timeout=10, data=Form_Data)
        except requests.exceptions.RequestException:
            Data['type'] = 'False'
            Data['msg'] = 'url链接超时'
            json_Data = json.dumps(Data)
            return json_Data
        Data['type'] = 'True'
        Data['msg'] = resp.json()
        json_Data = json.dumps(Data)
        return json_Data


class Graphing:  # 绘制图形类,把数据做成图片的形式

    def __init__(self, messages, Type=0):  # messages是个字典 Type 决定了该如何绘制图片
        self.type = Type
        self.messages = messages
        if self.type == 0:
            self.pyplt_0()
        elif self.type == 1:
            self.pyplt_1()
        elif self.type == 2:
            self.pyplt_2()
        elif self.type == 3:
            self.pyplt_3()
        elif self.type == 4:
            self.pyplt_4()

    def pyplt_0(self):
        message = self.messages
        title = message['msg']['newslist'][0]['news'][0]['title']
        print(message['msg']['newslist'][0]['news'][0]['title'])
        x = np.array([title, "Runoob-2", "Runoob-3", "C-RUNOOB"])  # 标题
        y = np.array([12, 22, 6, 18])  # 数据
        plt.bar(x, y)
        plt.savefig("debug.png")
        return 0

    def pyplt_1(self):
        pass

    def pyplt_2(self):
        pass

    def pyplt_3(self):
        pass

    def pyplt_4(self):
        pass


class gui:  # gui界面
    def __init__(self, messages):
        self.messages = messages

    def tkgui(self):
        messages = self.messages
        riskarea = messages['msg']['newslist'][0]['riskarea']['high'] + messages['msg']['newslist'][0]['riskarea'][
            'mid']
        print(riskarea)
        root = tk.Tk()
        sbar_right = tk.Scrollbar(root)  # 创建滚动条
        sbar_right.pack(side="right", fill="y")  # 滚动条贴边
        sbar_bottom = tk.Scrollbar(root, orient="horizontal")  # 创建滚动条
        sbar_bottom.pack(side="bottom", fill="x")  # 滚动条贴底
        msg = tk.Text(root, width=280, font=('微软雅黑', 10, 'bold'))
        button_off = tk.Button(root, text="关闭", command=root.quit)
        tk.Label(root, text="风险地区", fg="red", font=('Times', 10, 'bold italic')).pack()
        msg.pack()
        # tk.Message()
        for i in riskarea:
            msg.insert("end", i + "\n")
        sbar_right.config(command=msg.yview)  # 滚动条绑定
        sbar_bottom.config(command=msg.xview)  # 滚动条绑定
        tk.Button(root, text="第二个窗口", command=self.twogui).pack()
        tk.Button(root, text="第三个窗口", command=self.gui_2).pack()
        tk.Button(root, text="第四个窗口", command=self.gui_3).pack()
        tk.Button(root, text="第五个窗口", command=self.gui_4).pack()
        button_off.pack(side="bottom")
        root.title("疫情数据查询系统----by_曾大傻")
        root.geometry('650x500')
        root.mainloop()

    def twogui(self):
        root = tk.Toplevel()
        root.title("二级窗口")
        Graphing(a1)
        photo = ImageTk.PhotoImage(Image.open('debug.png'))
        print(photo)
        Lab = tk.Label(root, text='第一个图片测试', compound='center', font=('微软雅黑', 30), image=photo)
        Lab.pack()
        root.mainloop()

    def gui_2(self):
        pass

    def gui_3(self):
        pass

    def gui_4(self):
        pass


if __name__ == '__main__':
    a = Request_Data('http://api.tianapi.com/ncov/index', '2020-02-12').Get_Info()
    a1 = json.loads(a)
    datetime.datetime.strptime('2020-02-12', '%Y-%m-%d')
    print(type(a1))

    gui(a1).tkgui()
