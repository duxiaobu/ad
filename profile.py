import os
import xlrd
import argparse
import time
from spider import Spider


class Profile:
    def __init__(self):
        self.end_flag = 0

    def start(self):
        arguments = Profile.get_arguments()
        # 打开excel文件
        data = xlrd.open_workbook(arguments.path)
        # 根据sheet下标选择读取内容
        sheet = data.sheet_by_index(0)
        total_rows = sheet.nrows
        while self.end_flag < 10:
            for i in range(arguments.start, total_rows):
                info = sheet.row_values(i)
                state = info[5]
                city = info[6]
                # 如果资料不全，则切换资料
                if bool(state) is False or bool(city) is False:
                    self.end_flag += 1
                    print("资料不全")
                    continue
                # 根据城市切换IP
                command = f'start D:\soft\911\ProxyTool\AutoProxyTool.exe -ChangeProxy/US/{state}/"{city}" -citynolimit'
                os.system(command)
                # 同步等待3秒，等待IP切换成功
                time.sleep(3)
                spider = Spider()
                ua = spider.get_random_ua(arguments.ua_path)
                if bool(ua) is False:
                    raise Exception("ua解析失败")
                driver = spider.init_browser(ua)
                check = spider.check_ip(driver)
                if check is False:
                    self.end_flag += 1
                    print("IP检测失败")
                    continue

                spider.do_offers(driver, info)

        # 发送email通知
        pass

    @staticmethod
    def get_arguments():
        parser = argparse.ArgumentParser(description='解析资料')
        parser.add_argument('-info_path', type=str, default='E:\doc\data\information.xlsx', required=True, help="资料文件绝对地址")
        parser.add_argument('-info_start', type=int, default=0, required=True, help="资料起始位置")
        parser.add_argument('-ua_path', type=str, default='', required=True, help="ua绝对位置")
        args = parser.parse_args()
        return args


if __name__ == '__main__':
    profilePath = "E:\doc\data\information.xlsx"