

import os


def read_file(file):
    with open(file,encoding="utf-8") as f:
        read_all =f.read()
        f.close()
    return read_all

def rewrite_file(file,data):
    with open(file,"w",encoding="UTF-8") as f:
        f.write(data)
        f.close()


def replace(file,old_c,new_c):
    content = read_file(file)
    content = content.replace(old_c,new_c)
    rewrite_file(file,content)

# 1. 生成 gitbook电子书的列表--->直接让gitbook去编辑
#
def writeinti_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        f_output.write(data)
        f_output.write('\n')

# * [Java -parameters编译选项（获取参数名字）](Java -parameters编译选项（获取参数名字）.md)
if __name__=="__main__":

    for _,_,files in os.walk(os.getcwd()):
        file_list= [x for x in files if x !=  'md2html.py']
        for item in file_list:
            f_item = "".join("".join("".join(item.split("）")).split("（")).split())

            writeinti_file("list.txt","* [{0}]({1})".format(f_item[:-3],f_item))
