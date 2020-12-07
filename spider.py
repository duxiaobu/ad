import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.extend_sleep import random_sleep


class Spider:
    @staticmethod
    def get_random_ua(ua_path):
        """随机获取UA"""
        try:
            with open(ua_path, "r", encoding="utf8") as fp:
                uas = fp.readlines()
                index = random.randint(0, len(uas))
                return uas[index]
        except Exception as e:
            raise Exception("UA文件打开失败", e)

    @staticmethod
    def init_browser(ua):
        """初始化浏览器"""
        try:
            options = Options()  # 网上找到 你可以试试
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # 这里是你指定浏览器的路径
            # 更换UA
            options.add_argument(f'user-agent={ua}')
            driver = webdriver.Chrome(options=options)
            # 隐式等待时间
            driver.implicitly_wait(20)
            with open('./doc/stealth.min.js') as f:
                js = f.read()

            # 隐藏selenium痕迹
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": js
            })
            random_sleep(3)

            return driver
        except Exception as e:
            raise Exception("初始化浏览器失败", e)

    @staticmethod
    def check_ip(driver):
        """检查IP"""
        try:
            driver.get("http://mobivst.com/7roi/checkip/")
            if driver.title.startswith("代理"):
                return False
            driver.get("http://www.check2ip.com")
            element = driver.find_element_by_xpath("//td[text()='Country: ']/following-sibling::td")
            if element.text != "US":
                return False
            driver.get("http://www.whoer.net")
            element = driver.find_element_by_class_name("cont proxy-status-message")
            if element.text.strip() != "No":
                return False
            element = driver.find_element_by_xpath("//span[@class='value']")
            if element.text.strip() != "No":
                return False
            element = driver.find_element_by_xpath("//a[@rel='nofollow']")
            if element.text.strip() != "No":
                return False
            element = driver.find_element_by_xpath("//span[@data-fetched='country_code']")
            if element.text.strip() != "US":
                return False
            return True
        except Exception as e:
            return False

    @staticmethod
    def do_offers(driver, info):
        """run offer"""
        # FirstQuoteHealth
        driver.get("https://quote.firstquotehealth.com/quote")
        random_sleep(10)
        driver.find_element_by_class_name("button__submit e-preReg__button").click()
        random_sleep(10)
        # 性别
        params = "form-gender-female"
        if info[7] == "male":
            params = "form-gender-male"
        driver.find_element_by_xpath(f"//label[@for='{params}']").click()
        # 美国体重大概150-190cm
        driver.find_element_by_id("form-height-feet").send_keys(random.randint(5, 6))
        driver.find_element_by_id("form-height-inches").send_keys(random.randint(0, 11))
        # 美国体重大概130-250斤
        driver.find_element_by_id("form-weight").send_keys(random.randint(143, 273))
        # 出生日期
        driver.find_element_by_id("form-dob-month").send_keys(info[7])
        driver.find_element_by_id("form-dob-day").send_keys(info[7])
        driver.find_element_by_id("form-dob-year").send_keys(info[7])
        random_sleep(5)
        driver.find_element_by_class_name("m-transition-button nextStep").click()
        random_sleep(5)
        yes_no = ["yes", "no"]
        # 家庭成员
        driver.find_element_by_xpath(f"//label[@for='family-size-{random.randint(2, 7)}']").click()
        # 收入
        driver.find_element_by_xpath(f"//label[@for='income-{random.randint(1, 3)}']").click()
        # 重大事件
        events_list = ["Got Married", "Got Divorced", "Loss of Coverage", "Moved",
                       "Changed or Lost Job", "Birth or Adoption", "none_above"]
        driver.find_element_by_xpath(
            f"//label[@for='qualifying-events-{random.choice(events_list)}']").click()
        # 没有重大疾病
        driver.find_element_by_xpath("//label[@for='medical-conditions-none_above']").click()
        # 每周运动几次
        driver.find_element_by_xpath(f"//label[@for='frequencies-{random.randint(0, 2)}']").click()
        # 没有当兵
        driver.find_element_by_xpath("//label[@for='military-no']").click()
        # 保单人员没有怀孕
        driver.find_element_by_xpath("//label[@for='pregnant-no']").click()
        # 对远程医疗是否感兴趣
        driver.find_element_by_xpath(f"//label[@for='telehealth-{random.choice(yes_no)}']").click()
        # 是否抽烟
        driver.find_element_by_xpath(f"//label[@for='tobacco-{random.choice(yes_no)}']").click()
        # 不会买宠物保险
        driver.find_element_by_xpath("//label[@for='petInsurance-no']").click()
        # 当前是否参加了保险
        driver.find_element_by_xpath(f"//label[@for='medicare-{random.choice(yes_no)}']").click()
        random_sleep(5)
        driver.find_element_by_class_name("m-transition-button nextStep").click()
        random_sleep(5)
        # 什么时候需要保险
        driver.find_element_by_xpath(f"//label[@for='timeframe-{random.randint(0, 2)}']").click()
        # 对其他什么保险感兴趣
        insurance = ["dental", "vision", "life"]
        driver.find_element_by_xpath(f"//label[@for='{random.choice(insurance)}-insurance']").click()
        # 个人信息
        driver.find_element_by_id("form-firstname").send_keys(info[7])
        driver.find_element_by_id("form-register--last-name").send_keys(info[7])
        driver.find_element_by_id("form-address").send_keys(info[7])
        driver.find_element_by_id("form-city").send_keys(info[7])
        driver.find_element_by_xpath(f"//option[@value='{info[7]}']").click()
        driver.find_element_by_id("form-zip-code").send_keys(info[7])
        driver.find_element_by_id("form-register--phone-number").send_keys(info[7])
        driver.find_element_by_id("form-email").send_keys(info[7])
        random_sleep(10)
        driver.find_element_by_class_name("m-transition-button nextStep").click()
        random_sleep(5)
        # todo 需要处理后面弹出的quote


if __name__ == '__main__':
    spider = Spider()
