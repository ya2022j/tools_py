


#! -*- utf-8 -*-
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
# 导入网页驱动软件
from selenium import webdriver
# 导入WebDriverWait等待模块
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests








def list_null(list_content):
    if list_content !=[]:
        result = list_content
    else:
        result = ["null"]
    return result



def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
def readjsonfile(filename):
   with open(filename, 'r', encoding='utf-8') as fw:
      s = json.load(fw)
      return s





def screenshot_image(url,code,folder):
    driver = webdriver.PhantomJS(executable_path="C:\\Python310\\Scripts\\phantomjs.exe")
    # 访问的网址（以央视网为例）
    driver.get(url)
    # 最大化浏览器
    driver.maximize_window()

    # 截取登录框的页面保存到相应位置
    driver.save_screenshot('{1}{0}.jpg'.format(code,folder))

    # 模拟点击按钮跳转体育页面

    # 退出驱动关闭所有窗口
    driver.quit()

if __name__=="__main__":
    errorpath="C:\\jf_site\\error\\"
    normalpath="C:\\jf_site\\img\\"
    result = readjsonfile("nikki225_module.json")+readjsonfile("jpx400_module.json")
    for item in result:
        type_url = "http://127.0.0.1:5000/jp/{0}".format(item["type"])
        stock_url = "http://127.0.0.1:5000/jp/{0}".format(item["code"])

        type_result = requests.get(type_url)
        screenshot_image(stock_url, item["type"],normalpath)
        if type_result.status_code!=200:
            screenshot_image(stock_url, item["type"], errorpath)
            print(type_result)

        stock_result = requests.get(stock_url)
        screenshot_image(stock_url, item["code"], normalpath)
        if stock_result.status_code!=200:
            print(stock_url)
            screenshot_image(stock_url, item["code"], errorpath)













