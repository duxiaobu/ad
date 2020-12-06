import random
from selenium import webdriver


class Spider:
    def __init__(self):
        self.browser = webdriver.Chrome("E:\doc\chromDriver\chromedriver.exe")
        self.user_agent_path = "E:\\AD\\1.txt"

    @staticmethod
    def get_random_ua(ua_path):
        with open(ua_path, "r", encoding="utf8") as fp:
            uas = fp.readlines()
            index = random.randint(0, len(uas))
            return uas[index]

    def init_browser(self):
        ua =
        print(ua)
        self.browser.

if __name__ == '__main__':
    spider = Spider()
    spider.get_random_ua()
    print(random.randint(0, 200))
