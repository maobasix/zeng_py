import openpyxl
import datetime


class py_excel:
    def __init__(self, path):
        self.path = path

    def add_excel(self):
        cel = openpyxl.Workbook()
        cel.save(self.path)

    def del_excel(self):
        pass

    def alter_excel(self):
        pass

    def look_excel(self):
        pass


if __name__ == '__main__':
    py_excel(input("输入路径")).add_excel()
