

import os
import time




def remove_file(filename):
    for file in os.listdir("."):
        file_list = file.split(".")
        if len(file_list) != 1:
            os.remove(filename)




def zip_jieya(path,zipfilename):

    import zipfile
    try:
        with zipfile.ZipFile(zipfilename, mode="a") as f:
            f.extractall(path)  ##将文件解压到指定目录，解压密码为root
    except Exception as e:
        print("异常对象的类型是:%s" % type(e))
        print("异常对象的内容是:%s" % e)
    finally:
        f.close()
def check_zipfile(path,file):
    filepath = path + file

    isExists = os.path.exists(filepath)
    if isExists:
        zip_jieya(path,file)
        time.sleep(0.1)
        remove_file(filepath)

# crontab  */1 * * * 1-5   /usr/local/python3/bin/python3.8    /home/mk_m/crontab_scripts/check_update_cleanup_2json_by_type_jp_dtS.py
if __name__ == "__main__":
    check_path = "/home/scp_test/"
    check_file = "update_cleanup_2json_by_type_jp_dtS.zip"
    check_zipfile(check_path, check_file)



