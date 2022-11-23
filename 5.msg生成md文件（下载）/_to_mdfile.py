# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from requests.exceptions import RequestException
import csv
from lxml import etree
import json
# 1 各大指数制作json文件,代码,板块 。。。
# 2 保证都有效。财务数据模型再整理!每3天做一次采集!
# 3 指数,也就是市场的整体收益状况就有一个足够的把握。这个是除了技术之外的最最核心的基金交易的依据。

from selenium import webdriver
import time
import datetime
import pymysql
import requests
from lxml import etree

from sqlalchemy import create_engine
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType
driver = webdriver.Chrome()
def use_selenium_headless(url):
    # 为Chrome配置无头模式

    # 在启动浏览器时加入配置

    driver.get(url)
    html = driver.page_source
    return html



def writeintoTSV_file(filename,data):
    with open(filename, 'a', newline='\n', encoding="utf-8") as f_output:
        f_output.write(data)





def writeintoMD_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as f_output:
        f_output.write(data)

    # 菜鸟教程
def runoob_eburl(url,title):
    html = use_selenium_headless(url)




    # 菜鸟教程




    runoob_pattern = re.compile('<div class="article-body">(.*?)<div class="previous-next-links">', re.S)
    items = re.findall(runoob_pattern, html)


    for item in items:

        print(items)
        writeintoMD_file("{0}-{1}.md".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),title), item)
        # 顺便把写入的格式也写好
        # etitle = "* [{0}]({0}.md)".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        # writeintoTSV_file("etitle.txt", etitle+"\n")


    while True:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/a[1]').click()

        html = driver.page_source
        # 菜鸟教程

        runoob_pattern = re.compile('<div class="article-body">(.*?)<div class="previous-next-links">', re.S)
        items = re.findall(runoob_pattern, html)


        for item in items:
            print(items)
            writeintoMD_file("{0}-{1}.md".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), title), item)
            # 顺便把写入的格式也写好
            # etitle = "* [{0}]({0}.md)".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            # writeintoTSV_file("etitle.txt", etitle + "\n")


def runoob_eburl_example(url):
    html = use_selenium_headless(url)




    # 菜鸟教程




    title_pattern = re.compile('<h1>(.*?)</h1>', re.S)
    title = re.findall(title_pattern, html)

    runoob_pattern = re.compile('<div class="article-body">(.*?)<div class="previous-next-links">', re.S)
    items = re.findall(runoob_pattern, html)

    for item in items:
        print(items)
        writeintoMD_file("{0}.md".format("".join(title[1].split())),item)



def weixueyuan_eburl_forhugo(url):
    html = use_selenium_headless(url)

    weixueyuan_pattern = re.compile('<div id="arc-body-top" class="arc-body">(.*?)<div id="nice-arcs"', re.S)
    items = re.findall(weixueyuan_pattern, html)
    title_pattern = re.compile("<h1>(.*?)</h1>", re.S)
    title_list = re.findall(title_pattern, html)

    for item in items:
        print(items)
        writeintoMD_file("{0}.md".format(title_list[0]), item)






def bb_eburl_forhugo(url):
    driver.get(url)
    html = driver.page_source

    #  //a/@href

    element = etree.HTML(html)

    half_url = element.xpath('//*[@id="leftcolumn"]/a/@href')
    for item in half_url:
        driver.get("http://www.codebaoku.com"+item)
        html = driver.page_source
        weixueyuan_pattern = re.compile('<div class="article-body">(.*?)<div class="fivecol right-column">', re.S)
        items = re.findall(weixueyuan_pattern, html)
        title_pattern = re.compile("<h1>(.*?)</h1>", re.S)
        title_list = re.findall(title_pattern, html)


        for item in items:
            print(items)
            writeintoMD_file("{0}.md".format(title_list[0]), item)
            time.sleep(1)









def runoob_eburl_forhugo(url,title):
    html = use_selenium_headless(url)


    runoob_pattern = re.compile('<div class="article-body">(.*?)<div class="previous-next-links">', re.S)
    items = re.findall(runoob_pattern, html)


    for item in items:

        print(items)
        writeintoMD_file("{0}-{1}.md".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),title), item)


    while True:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/a[1]').click()
        html = driver.page_source

        runoob_pattern = re.compile('<div class="article-body">(.*?)<div class="previous-next-links">', re.S)
        items = re.findall(runoob_pattern, html)
        for item in items:
            print(items)
            writeintoMD_file("{0}-{1}.md".format(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), title), item)







if __name__ == "__main__":
    l =  ["https://www.runoob.comjava/method-break.html","https://www.runoob.comjava/method-continue.html","https://www.runoob.comjava/method-label.html","https://www.runoob.comjava/method-enum.html","https://www.runoob.comjava/method-enum1.html","https://www.runoob.comjava/method-for.html","https://www.runoob.comjava/method-varargs.html","https://www.runoob.comjava/method-varargs1.html","https://www.runoob.com/java/java-print-diamond.html","https://www.runoob.com/java/java-print-multiplicationtable.html","https://www.runoob.com/java/java-print-the-triangle.html","https://www.runoob.com/java/java-print-invertedtriangle.html","https://www.runoob.com/java/java-print-parallelogram.html","https://www.runoob.com/java/java-print-rect.html","https://www.runoob.com/java/file-write.html","https://www.runoob.com/java/file-read.html","https://www.runoob.com/java/file-delete.html","https://www.runoob.com/java/file-copy.html","https://www.runoob.com/java/file-append.html","https://www.runoob.com/java/file-create-temp.html","https://www.runoob.com/java/file-date-modify.html","https://www.runoob.com/java/file-size.html","https://www.runoob.com/java/file-rename.html","https://www.runoob.com/java/file-read-only.html","https://www.runoob.com/java/file-exist.html","https://www.runoob.com/java/file-dir.html","https://www.runoob.com/java/file-date.html","https://www.runoob.com/java/file-create.html","https://www.runoob.com/java/file-compare.html","https://www.runoob.com/java/dir-create.html","https://www.runoob.com/java/dir-delete.html","https://www.runoob.com/java/dir-empty.html","https://www.runoob.com/java/dir-hidden.html","https://www.runoob.com/java/dir-size.html","https://www.runoob.com/java/dir-search.html","https://www.runoob.com/java/dir-parent.html","https://www.runoob.com/java/dir-modification.html","https://www.runoob.com/java/dir-hierarchy.html","https://www.runoob.com/java/dir-display.html","https://www.runoob.com/java/dir-sub.html","https://www.runoob.com/java/dir-search-file.html","https://www.runoob.com/java/dir-root.html","https://www.runoob.com/java/dir-current.html","https://www.runoob.com/java/dir-traverse.html","https://www.runoob.com/java/exception-method.html","https://www.runoob.com/java/exception-hierarchy.html","https://www.runoob.com/java/exception-finally.html","https://www.runoob.com/java/exception-catch.html","https://www.runoob.com/java/exception-thread.html","https://www.runoob.com/java/exception-printstack.html","https://www.runoob.com/java/exception-overloaded-method.html","https://www.runoob.com/java/exception-chain.html","https://www.runoob.com/java/exception-user.html","https://www.runoob.com/java/data-add.html","https://www.runoob.com/java/data-intopost.html","https://www.runoob.com/java/data-insert.html","https://www.runoob.com/java/data-element.html","https://www.runoob.com/java/data-replace.html","https://www.runoob.com/java/data_linklist.html","https://www.runoob.com/java/data-vecsort.html","https://www.runoob.com/java/data-stack.html","https://www.runoob.com/java/data-search.html","https://www.runoob.com/java/data-reverse.html","https://www.runoob.com/java/data-queue.html","https://www.runoob.com/java/data-vec-max.html","https://www.runoob.com/java/data-update.html","https://www.runoob.com/java/data-swap.html","https://www.runoob.com/java/collection-array.html","https://www.runoob.com/java/collection-compare.html","https://www.runoob.com/java/collection-iterate.html","https://www.runoob.com/java/collection-size.html","https://www.runoob.com/java/collection-shuffle.html","https://www.runoob.com/java/collection-iterator.html","https://www.runoob.com/java/collection-reverse.html","https://www.runoob.com/java/collection-remove.html","https://www.runoob.com/java/collection-readonly.html","https://www.runoob.com/java/collection-print.html","https://www.runoob.com/java/collection-conversion.html","https://www.runoob.com/java/collection-rotate.html","https://www.runoob.com/java/collection-minmax.html","https://www.runoob.com/java/collection-hashtable-key.html","https://www.runoob.com/java/collection-enumeration.html","https://www.runoob.com/java/collection-all.html","https://www.runoob.com/java/collection-replace.html","https://www.runoob.com/java/collection-sublist.html","https://www.runoob.com/java/net-address.html","https://www.runoob.com/java/net-port.html","https://www.runoob.com/java/net-localip.html","https://www.runoob.com/java/net-serverfile.html","https://www.runoob.com/java/net-multisoc.html","https://www.runoob.com/java/net-filetime.html","https://www.runoob.com/java/net-connected.html","https://www.runoob.com/java/net-webpage.html","https://www.runoob.com/java/net-urldate.html","https://www.runoob.com/java/net-url-header.html","https://www.runoob.com/java/net-url.html","https://www.runoob.com/java/net-serversocket-socket.html","https://www.runoob.com/java/thread-alive.html","https://www.runoob.com/java/thread-name.html","https://www.runoob.com/java/thread-monitor.html","https://www.runoob.com/java/thread-getpri.html","https://www.runoob.com/java/thread-deadlock.html","https://www.runoob.com/java/thread-id.html","https://www.runoob.com/java/thread-suspend.html","https://www.runoob.com/java/thread-stop.html","https://www.runoob.com/html/thread-procon.html","https://www.runoob.com/java/thread-status.html","https://www.runoob.com/java/thread-showall.html","https://www.runoob.com/java/thread-priorityinfo.html","https://www.runoob.com/java/thread-interrupt.html"]
    l.sort(reverse=True)

    for url in l:
        try:

            runoob_eburl_example(url)
        except:
            continue






