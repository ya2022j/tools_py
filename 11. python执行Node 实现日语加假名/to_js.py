#! -*- coding:utf-8 -*-



import os
import sys
import importlib
importlib.reload(sys)



# # 1. 修改js文件的入力内容
# # 2. 执行命令行，然后输出转换的内容
#

from subprocess import check_output




def from_node_translate(jsfile,content):
    # 创建一个变量并存储我们要搜索的文本
    search_text = "ja_content"

    # 创建一个变量并存储我们要添加的文本
    replace_text = content

    # 使用 open() 函数以只读模式打开我们的文本文件
    with open(jsfile, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()

        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text, replace_text)

    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(jsfile, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)

    # 打印文本已替换
    print("文本已替换")


    bytesTxt = check_output("node {0}".format(jsfile), timeout=100)


    # 文本最后还要还原成  ja_content





    # 创建一个变量并存储我们要搜索的文本
    search_text = content

    # 创建一个变量并存储我们要添加的文本
    replace_text = "ja_content"

    # 使用 open() 函数以只读模式打开我们的文本文件
    with open(jsfile, 'r', encoding='UTF-8') as file:
        # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
        data = file.read()

        # 使用 replace() 函数搜索和替换文本
        data = data.replace(search_text, replace_text)

    # 以只写模式打开我们的文本文件以写入替换的内容
    with open(jsfile, 'w', encoding='UTF-8') as file:
        # 在我们的文本文件中写入替换的数据
        file.write(data)


    print("文本恢复")
    return  bytesTxt.decode('utf8').strip()





print(from_node_translate("nodejs_translate.js","'通り'"))
