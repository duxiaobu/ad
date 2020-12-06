import os
import xlrd
import argparse
import time


class Profile:
    @staticmethod
    def start():
        arguments = Profile.get_arguments()
        print(arguments.path, arguments.start)
        # 打开excel文件
        data = xlrd.open_workbook(arguments.path)
        # 根据sheet下标选择读取内容
        sheet = data.sheet_by_index(0)
        total_rows = sheet.nrows
        for i in range(arguments.start, total_rows):
            state = sheet.row_values(i)[5]
            city = sheet.row_values(i)[6]
            # 根据城市切换IP
            command = f'start D:\soft\911\ProxyTool\AutoProxyTool.exe -ChangeProxy/US/{state}/"{city}" -citynolimit'
            os.system(command)
            # 同步等待3秒，等待IP切换成功
            time.sleep(3)

    @staticmethod
    def get_arguments():
        parser = argparse.ArgumentParser(description='解析资料')
        parser.add_argument('-path', type=str, default='E:\doc\data\information.xlsx', required=True, help="资料文件绝对地址")
        parser.add_argument('-start', type=int, default=0, required=True, help="资料起始位置")
        args = parser.parse_args()
        return args


if __name__ == '__main__':
    profilePath = "E:\doc\data\information.xlsx"
    profile = Profile(profilePath)
    profile.parse_data()
