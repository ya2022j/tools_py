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


if __name__=="__main__":
    file_list = []
    for _,_,files in os.walk(os.getcwd()):
        file_list= [replace(x, "菜鸟教程", "itbenkyou") for x in files if x !=  'replace_kw.py']
        file_list= [replace(x, "微学苑", "itbenkyou") for x in files if x !=  'replace_kw.py']
        file_list= [replace(x, "runoob", "itbenkyou") for x in files if x !=  'replace_kw.py']
        file_list= [replace(x, "runoob.com", "itbenkyou.com") for x in files if x !=  'replace_kw.py']
        file_list= [replace(x, "weixueyuan", "itbenkyou") for x in files if x !=  'replace_kw.py']
        file_list= [replace(x, "weixueyuan.net", "itbenkyou.com") for x in files if x !=  'replace_kw.py']


