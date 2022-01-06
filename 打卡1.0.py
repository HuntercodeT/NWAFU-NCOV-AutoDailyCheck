from selenium import webdriver
import time
import requests

def daka(path,usernumber,pwd):
    '''
    通过selenium启动电脑的edge浏览器，全程模拟人工动作，实现密码输入的登录和点击等各项操作
    推荐使用edge浏览器，也可以使用别的浏览器，但不知道为什么我的chrome即便给了打卡网站的位置权限还是获取不到地址，故我使用了edge浏览器，
    '''

    url = 'https://app.nwafu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.nwafu.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex'

    browser = webdriver.Edge(path)
    #打卡登陆界面
    browser.get(url)
    user = browser.find_element_by_xpath('//input[@type="text"]')
    # print(user)
    time.sleep(2)

    #输入账号和密码
    user.send_keys(usernumber)
    time.sleep(2)
    password = browser.find_element_by_xpath('//input[@type="password"]')
    time.sleep(2)
    password.send_keys(pwd)
    time.sleep(2)

    # 点击登录
    login = browser.find_element_by_xpath('//div[@class="btn"]')
    login.click()
    time.sleep(5)
    # 点击获取位置并点击
    location = browser.find_element_by_xpath('//input[@placeholder="点击获取地理位置"]')
    location.click()
    time.sleep(5)

    # 模拟滑动页面 感觉可有可无
    js='document.documentElement.scrollTop=100000'
    browser.execute_script(js)
    time.sleep(5)
    # 获取提交信息按钮并点击
    submit = browser.find_element_by_xpath('//div[@class="footers"]/a')
    submit.click()
    time.sleep(5)
    try:
        try:
            # 获取确认提交信息按钮并点击
            enter = browser.find_element_by_xpath('//div[@class="wapcf-btn wapcf-btn-ok"]')
            enter.click()
            time.sleep(3)
            tishi = browser.find_element_by_xpath('//div[@class="wapat-title"]').text
            message = '签到成功'
        except :
            sure = browser.find_element_by_xpath('//div[@class="wapat-btn wapat-btn-ok"]')
            sure.click()
            time.sleep(3)
            message = '你已签到过，请勿重复提交'
    except Exception as e:
        message = '打卡错误\n' + '错误提示为：' + str(e)
    browser.close()
    return message

def push(token,message):
    '''通过pushplus向微信推送消息，消息内容为message变量，模板为json，不是很好看凑合用，可自行修改'''
    url = 'http://pushplus.hxtrip.com/send/'
    data = {
        'token':token,
        "title":"西农健康打卡",
        "content":message,
        'template':'json'
    }
    requests.post(url,data=data)

if __name__ == '__main__':
    usernumber = '1234567891'                                   #学号
    pwd = 'abcd4561'                                            #密码
    token = 'dsa24533455245321ds2asd4f5a2sa2d'                  #pushplus的token，没有可不填
    path = 'F:\PYTHON\msedgedriver.exe'                         #浏览器驱动存放路径，填到.exe文件本身
    message = daka(path,usernumber,pwd)
    if len(token) != 0:
        push(token,message)
    else:print(message)

