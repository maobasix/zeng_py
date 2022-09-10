import os
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


def del_png(png_name):
    os.remove(png_name)


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

    def pyplt_0(self):
        message = self.messages
        title = message['msg']['newslist'][0]['news'][0]['title']
        plt.title(title)
        riskare = message['msg']['newslist'][0]['riskarea']['high'] + message['msg']['newslist'][0]['riskarea'][
            'mid']
        print(riskare)
        riskare.sort(reverse=True)
        print(riskare)

        def array_count(i):
            risk_str = str(riskare[i])
            i_array = risk_str.split('·')
            return i_array[0]

        a_c = 0
        x_title = []
        y_cout = []
        for i in range(len(riskare)):
            i_array_start = array_count(i)
            try:
                if i_array_start == array_count(i + 1):
                    a_c += 1
                else:
                    x_title.append(i_array_start)
                    y_cout.append(a_c)
                    a_c = 0
            except:
                pass

        plt.bar(np.array(x_title), np.array(y_cout))
        plt.savefig("debug.png")
        plt.figure()
        return 0

    def pyplt_1(self):
        message = self.messages
        title = message['msg']['newslist'][0]['news'][0]['title']
        plt.title(title)
        riskare = message['msg']['newslist'][0]['riskarea']['high'] + message['msg']['newslist'][0]['riskarea'][
            'mid']
        print(riskare)
        riskare.sort(reverse=True)
        print(riskare)

        def array_count(i):
            risk_str = str(riskare[i])
            i_array = risk_str.split('·')
            return i_array[0]

        a_c = 0
        x_title = []
        y_cout = []
        for i in range(len(riskare)):
            i_array_start = array_count(i)
            try:
                if i_array_start == array_count(i + 1):
                    a_c += 1
                else:
                    x_title.append(i_array_start)
                    y_cout.append(a_c)
                    a_c = 0
            except:
                pass
        print(len(x_title), len(y_cout))
        print(x_title)
        plt.plot(x_title, y_cout)
        plt.savefig("debug1.png")
        plt.figure()
        return 0


class gui:  # gui界面
    def __init__(self, messages):
        self.messages = messages

    def tkgui(self):
        messages = self.messages
        riskarea = messages['msg']['newslist'][0]['riskarea']['high'] + messages['msg']['newslist'][0]['riskarea'][
            'mid']
        print("riskarea类型：", type(riskarea))
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
        tk.Button(root, text="第二个窗口", command=self.gui_1).pack()
        tk.Button(root, text="第三个窗口", command=self.gui_2).pack()
        tk.Button(root, text="第四个窗口", command=self.gui_3).pack()
        button_off.pack(side="bottom")
        root.title("疫情数据查询系统")
        root.geometry('650x500')
        root.mainloop()

    def gui_1(self):
        root = tk.Toplevel()
        root.title("二级窗口")
        Graphing(a1)
        photo = ImageTk.PhotoImage(Image.open('debug.png'))
        print(photo)
        Lab = tk.Label(root, compound='center', font=('微软雅黑', 30), image=photo)
        Lab.pack()
        root.mainloop()
        del_png('debug.png')

    def gui_2(self):
        root = tk.Toplevel()
        Graphing(a1, 1)
        root.title("二级窗口")
        photo = ImageTk.PhotoImage(Image.open('debug1.png'))
        print(photo)
        Lab = tk.Label(root, compound='center', font=('微软雅黑', 30), image=photo)
        Lab.pack()
        root.mainloop()
        del_png('debug1.png')

    def gui_3(self):
        messages = self.messages
        root = tk.Toplevel()
        root.title("二级窗口")
        currentConfirmedCount = messages['msg']['newslist'][0]['desc']['currentConfirmedCount']  # 现存确诊
        confirmedCount = messages['msg']['newslist'][0]['desc']['confirmedCount']  # 累计确诊
        curedCount = messages['msg']['newslist'][0]['desc']['curedCount']  # 累计治愈
        deadCount = messages['msg']['newslist'][0]['desc']['curedCount']  # 累计死亡
        seriousCount = messages['msg']['newslist'][0]['desc']['seriousCount']  # 累计无症状
        highDangerCount = messages['msg']['newslist'][0]['desc']['highDangerCount']  # 国内高风险地区个数
        midDangerCount = messages['msg']['newslist'][0]['desc']['midDangerCount']  # 国内中风险地区个数
        msg = tk.Text(root, width=280, font=('微软雅黑', 10, 'bold'))
        msg.pack()
        meg = "现存确诊:{}人\n 累计确诊:{}人\n 累计治愈:{}人\n 累计死亡:{}人\n 累计无症状:{}人\n 国内高风险地区:{}个\n 国内中风险地区:{}个".format(
            currentConfirmedCount, confirmedCount, curedCount, deadCount, seriousCount, highDangerCount, midDangerCount)
        msg.insert("end", meg)
        root.mainloop()


if __name__ == '__main__':
    a = Request_Data('http://api.tianapi.com/ncov/index', '2020-02-12').Get_Info()
    a1 = json.loads(a)
    datetime.datetime.strptime('2020-02-12', '%Y-%m-%d')
    print(type(a1))

    gui(a1).tkgui()
