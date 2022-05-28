import requests
import datetime
import json

Data = {}


class Request_Data:  # 数据收集类
    def __init__(self, url, Time):
        self.Time = Time
        self.url = url

    def Get_Info(self):  # 收集函数
        try:
            datetime.datetime.strptime(self.Time, '%Y-%m-%d')
        except ValueError:
            print("时间格式错误")
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


class Data_Processing:  # 数据处理类
    def __init__(self):
        pass


class Graphing:  # 绘制图形类
    pass


'''if __name__ == '__main__':
    a = Request_Data('http://api.tianapi.com/ncov/index', '2020-02-12').Get_Info()
    a1 = json.loads(a)
    datetime.datetime.strptime('2020-02-12', '%Y-%m-%d')
    print(a1)
'''