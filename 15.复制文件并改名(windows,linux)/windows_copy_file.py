import os

import datetime

new_html = os.path.join(os.path.join(os.getcwd(), "templates"), "{0}.html".format("esee"))


# cp -i 原文件 目的路径/重命名文件  linux  os.system("cp -i search_module.html  {0}".format(new_html))
import shutil
def copyfile(oldfilename, newfilename):
    shutil.copy(oldfilename, newfilename)


#
# copyfile("search_module.html",new_html)

# 复制到文件所在目录的同级文件夹中




def peer_replicate(filename,dirname):
    newfile = os.path.join(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), dirname),
                           filename)
    copyfile(filename, newfile)

newfile= os.path.join(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),"device"),"d.json")
copyfile("d.json",new_html)

# '''***获取当前目录***'''
# print(os.getcwd())
# print(os.path.abspath(os.path.dirname(__file__)))
#
# '''***获取上级目录***'''
# print()
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))
#
# '''***获取上上级目录***'''
# print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
# -----------------------------------
# python os 获取当前目录上一级目录
# https://blog.51cto.com/u_15064655/3710000