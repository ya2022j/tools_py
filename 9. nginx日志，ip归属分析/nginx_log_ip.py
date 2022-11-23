#!/usr/bin/env python
#-*-coding:utf8-*-
"""
分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
"""
ip_list=[] #定义空列表 所有的访问IP放置在该列表中
ip_count={}#定义一个空字典 将IP和访问的次数放置到该字典中



import copy
import re
import json
import time

import requests
from lxml import etree
import datetime
import csv
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
import os
import os
ch_options = webdriver.ChromeOptions()
# 为Chrome配置无头模式
ch_options.add_argument("--headless")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')
# 在启动浏览器时加入配置
driver = webdriver.Chrome(options=ch_options)


def use_selenium_headless_getdt(url):
    driver.get(url)
    html = driver.page_source
    return html

def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
def to_fetch_ip_info(filename):
    """
    分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
    """
    ip_list = []  # 定义空列表 所有的访问IP放置在该列表中
    ip_count = {}  # 定义一个空字典 将IP和访问的次数放置到该字典中
    with  open(filename, "r") as ngfile:  # 打开日志文件
        for line in ngfile:
            # print(line.split())  调试信息
            ip_list.append(line.split()[0])  # 用split分割字符串获取到列表line.split()[0] 每行的IP地址
    for count in set(ip_list):  # 将ip_list去重
        ip_number = ip_list.count(count)  # 统计每个IP出现的次数
        ip_count.setdefault(count, ip_number)  # 将IP以及数量更新到字典
    ip_count_new = sorted(ip_count.items(), key=lambda d: d[1], reverse=True)  # 使用lambda函数 对其重新排序构建新字典
    for eachip in ip_count_new:
        ip_item_info = eachip[0]
        ip_item_times = eachip[1]
        print(ip_item_times, ip_item_info)
        # from selenium import webdriver
        # from selenium.webdriver.common.by import By
        # driver = webdriver.Chrome()
        # url = "https://rakko.tools/tools/11/"
        # driver.get(url)  # 打开有道翻译首页
        # e = driver.find_element(By.ID, 'serchIp')
        # e.send_keys(ip_item_info)
        # time.sleep(1)
        # html = driver.page_source
        # pattern_str = '<tr><th>国</th><td><img class="country_flg" src="../../image/flgIcon/fr.svg"><span class="country_name">(.*?)</span></td></tr>'
        # pattern = re.compile(pattern_str, re.S)
        # items = re.findall(pattern, html)
        # print(items)

        #

# <tbody><tr><td><span class="c-gap-right">IP地址:&nbsp;188.165.87.108</span>法国上法兰西格拉沃利讷</td></tr></tbody>


        # selector = etree.HTML(ret)
        # url_code = selector.xpath('//*[@id="1"]/div[1]/div[1]/div[2]/table/tbody/tr/td/text()')
        # # location_info_pattern='<tbody><tr><td><span class="c-gap-right">IP地址:&nbsp;{0}</span>(.*?)</td></tr></tbody>'.format(ip_item_info)
        # # location_info_items = re.findall(re.compile(location_info_pattern,re.S),ret)
        # print(ip_item_times,ip_item_info,url_code)
        # f_location = location_area[0].split()
        # loca_1 = None
        # loca_2 = None
        # loca_3 = None
        # loca_4 = None
        # if len(f_location) == 3:
        #     loca_1 = f_location[0]
        #     loca_2 = f_location[1]
        #     loca_3 = f_location[2]
        #     loca_4 = ""
        # elif len(f_location) == 2:
        #     loca_1 = f_location[0]
        #     loca_2 = f_location[1]
        #     loca_3 = ""
        #     loca_4 = ""
        # elif len(f_location) == 1:
        #     loca_1 = f_location[0]
        #     loca_2 = ""
        #     loca_3 = ""
        #     loca_4 = ""
        # elif len(f_location) == 4:
        #     loca_1 = f_location[0]
        #     loca_2 =  f_location[1]
        #     loca_3 =  f_location[2]
        #     loca_4 =  f_location[3]
        # else:
        #     pass
        # if len(location_operator) != 0:
        #     f_location_operator= location_operator[0]
        # else:
        #     f_location_operator  =""
        # f_data = [ip_item_info,loca_1,loca_2,loca_3,loca_4,f_location_operator,ip_item_times]
        # print(f_data)
        # writeintoTSV_file("{0}.tsv".format(datetime.datetime.now().strftime("%Y%m%d")),f_data)

#
if __name__ == "__main__":
    to_fetch_ip_info("access_20221121.log")