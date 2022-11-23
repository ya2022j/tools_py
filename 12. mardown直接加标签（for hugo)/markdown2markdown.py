


#coding:utf-8
import os
import datetime

'''
def rename(dirpath, oldext, newext):
    for roots, dirs, files in os.walk(dirpath):        
        for name in files:
            if name.endswith(oldext):      
                curdir = os.getcwd()            
                os.chdir(roots)             
                os.rename(name, os.path.splitext(name)[0] + newext)                
                os.chdir(curdir)

rename('/Users/black3y/Desktop/1/','.txt','.py')
'''

def filerename(filepath,srctype,destype):
    for path,dirlist,filelist in os.walk(filepath):
        for file in filelist:

            #防止文件名中包含.
            fullist = file.split('.')
            namelist = fullist[0:-1]
            filename = ''
            for i in namelist:
                filename = filename + i + '.'
            # print (filename)

            curndir = os.getcwd()    #获取当前路径
            # print (curndir)

            os.chdir(path)            #设置当前路径为目标目录
            newdir = os.getcwd()    #验证当前目录
            # print (newdir)

            filetype = file.split('.')[-1]    #获取目标文件格式

            if filetype == srctype:    #修改目标目录下指定后缀的文件（包含子目录）
                os.rename(file,filename+destype)

            if srctype == '*':        #修改目标目录下所有文件后缀（包含子目录）
                os.rename(file,filename+destype)

            if srctype == 'null':    #修改目标目录下所有无后缀文件（包含子目录）
                if len(fullist) == 1:
                    os.rename(file,file+'.'+destype)

            os.chdir(curndir)    #回到之前的路径

filerename(os.getcwd(),'md','html')

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

