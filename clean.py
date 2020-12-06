import os, subprocess, io

command = "start D:\soft\911\ProxyTool\AutoProxyTool.exe -ChangeProxy/US/MO/'joliet' -citynolimit"
# result = os.system(command)
# print(result)

if __name__ == '__main__':
    # proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    # print(proc.stdout.read())
    # print('------------')
    # print(proc.communicate())
    from selenium import webdriver

    chromedriver = "E:\doc\chromDriver\chromedriver.exe"

    browser = webdriver.Chrome(chromedriver)

    browser.get("https://www.baidu.com")

    # 获取当前的handle名字

    handle = browser.current_window_handle

    print("当前的handle：", handle)