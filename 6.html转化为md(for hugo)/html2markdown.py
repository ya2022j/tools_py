#! -*- utf-8 -*-
import os

import datetime


import random,string


# 1. 中文命名没有问题
# 2. 格式要注意

#+++
# title = "(Hu)go Template Primer"
# description = "这里是副标题"
# tags = [
#     "go",
#     "golang",
#     "templates",
#     "themes",
#     "development",
#     "日本語",
# ]
# date = "2014-04-02"
# categories = [
#     "Development",
#     "golang",
# ]
# +++



# 技术栈： python  golang
tags ="Java"

# Chinese 日语等
categories ="Chinese"


import html2text
for root,dirs,files in os.walk(os.getcwd(),topdown=True):
    for name in files:
        path = os.path.join(root,name)
        if path.endswith(".html"):
            title = os.path.splitext(name)[0]
            with open(path,encoding="utf-8") as html,open(os.path.join(root,title+".md"),"w",encoding="utf-8") as md:
                markdown = html2text.html2text(html.read())
                # 2022-07-28 23:20:28
                # 时间减去2天
                print(markdown)
                date_ = (datetime.datetime.now()+datetime.timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S")
                hugo_text = '+++\ntitle = "{0}"\ntags = [\n"{1}",\n"{2}",\n]\ndate = "{3}"\ncategories = [\n"{2}",\n]\n+++\n'.format(title,tags,categories,date_)

                md.writelines(hugo_text)
                md.write(markdown)
