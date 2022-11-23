
#! -*- coding:utf-8 -*-
import copy
import json
import os


#1. 创建文件夹，然后把文件复制到文件夹中，压缩文件夹 ---->批量压缩进入tar文件
#2. 传送
#3. 自动解压缩


from inspect import currentframe, getframeinfo

import zipfile
import os

def zip_yasuo(filename,zipfilename):
    import zipfile
    try:
        with zipfile.ZipFile(zipfilename, mode="a") as f:
            f.write(filename)  # #追加写入压缩文件
    except Exception as e:
        print("异常对象的类型是:%s" % type(e))
        print("异常对象的内容是:%s" % e)
    finally:
        f.close()

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

if __name__ == "__main__":

    frameinfo = getframeinfo(currentframe())
    current_filename = os.path.basename(frameinfo.filename)
    remove_py_currentfilename =current_filename.split(".py")[0]
    current_filename_zip = remove_py_currentfilename+ ".zip"
    #
    lpath = os.getcwd()
    # for dir_path, dir_names, file_names in os.walk(lpath):
    #     for item in file_names:
    #         if item != current_filename:
    #             zip_yasuo(item,"{0}.zip".format(remove_py_currentfilename))
    #
    #
    zip_jieya(lpath,current_filename_zip)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def readjsonfile(filename):
#     with open(filename, 'r', encoding='utf-8') as fw:
#         s = json.load(fw)
#         return s
#
#
# def writeinto_jsonfile(filename, list_data):
#     with open(filename, 'w', encoding='utf-8') as fw:
#         json.dump(list_data, fw, indent=4, ensure_ascii=False)
#
#
# def positive_2_negative_count(list_conntent, key_param,short_name):
#     list_conntent.sort(key=lambda x:(x[key_param]),reverse=True)
#
#     positive_num = len([x[key_param] for x in list_conntent if x[key_param] > 0])
#     negative_num = len([x[key_param] for x in list_conntent if x[key_param] < 0])
#     max_value_st = list_conntent[0][short_name]
#     max_value_st_change_r = list_conntent[0]["change_r"]
#     max_value_st_change_r_float = list_conntent[0]["change_r_float"]
#     max_value_st_short_name_html = list_conntent[0]["short_name_html"]
#     return positive_num, negative_num,max_value_st,max_value_st_change_r,max_value_st_change_r_float,max_value_st_short_name_html
#
# import os
#
# def scaner_file (window_path):
#     path_list = []
#     file = os.listdir(window_path)
#     for f in file:
#         read_path = os.path.join(window_path,f)
#         path_list.append(read_path)
#     return path_list
#
#
# # 1. 遍历目录下的所有文件
# # 2. 再遍历上传
#
# def scp_jsonfile_without_pwd(local_path,remote_path,remote_ip,filename):
#     local_file = local_path+"/device/"+filename
#     cmd = "scp -i 167id_rsa {0}  root@{1}:{2}".format(local_file,remote_ip,remote_path)
#     result = os.popen(cmd)
#
#     writeinto_jsonfile("check_cmd",[x for x in result])
#
#
#
#
#
#
#
# import datetime
# import sys
# import time
#
#
# # "15:32:55"
# # 在特定时间停止函数的装饰器和函数
#
#
# def at_sometime_exit(parameter):
#     print(parameter)
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             ret = func(*args,**kwargs)
#             while True:
#                 print("ssss")
#                 now_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
#                 stop_timeline = datetime.datetime.strptime(parameter, "%H:%M:%S")
#                 print(now_time)
#                 print(stop_timeline)
#                 time.sleep(1)
#                 if now_time > stop_timeline:
#                     print("ok")
#                     sys.exit(0)
#                 return ret
#         return inner
#     return wrapper
#
# def regular_time_exit(stop_time):
#     while True:
#         print("ssss")
#         now_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")
#         stop_timeline = datetime.datetime.strptime(stop_time, "%H:%M:%S")
#         print(now_time)
#         print(stop_timeline)
#         time.sleep(1)
#         if now_time>stop_timeline:
#             print("ok")
#             sys.exit(0)
#
# def f_func():
#
#     nikki225file =  "/home/dt_server/device/nikki225_module.json"
#     jpx400file =  "/home/dt_server/device/jpx400_module.json"
#
#     seen = set()
#     only_list = []
#     static_type_result = []
#     result = readjsonfile(nikki225file) + readjsonfile(jpx400file)
#     for item in result:
#         if item["code"] not in seen:
#             only_list.append(item)
#             seen.add(item["code"])
#     type_dict = {}
#
#     for  item  in only_list:
#         if item["type"] not in type_dict:
#             type_dict[item["type"]] = [item]
#         else:
#             type_dict[item["type"]].append(item)
#
#     print(len(only_list))
#     for k,v in type_dict.items():
#         for_cout_v = copy.deepcopy(v)
#
#
#         # 这里对于板块的收益率做一个排序
#         v.sort(key=lambda x: (x["change_r_float"]), reverse=True)
#
#         writeinto_jsonfile("/home/dt_server/device/{0}.json".format(k),v)
#         time.sleep(0.1)
#         scp_jsonfile_without_pwd(local_path, remote_path, remote_ip, "{0}.json".format(k))
#         positive_num, negative_num,max_value_st,max_value_st_change_r,max_value_st_change_r_float,max_value_st_short_name_html = positive_2_negative_count(for_cout_v,"change_r_float","short_name")
#         static_type = {}
#         static_type["type"] = k
#         static_type["positive_num"] = positive_num
#         static_type["negative_num"] = negative_num
#         static_type["top_up_stock"] = max_value_st
#         static_type["change_r"] = max_value_st_change_r
#         static_type["change_r_float"] = max_value_st_change_r_float
#         static_type["short_name_html"] = max_value_st_short_name_html
#         static_type["type_html"] =  '<a href=\"/jp/{0}\">{0}</a>'.format(k)
#         static_type_result.append(static_type)
#
#     writeinto_jsonfile("/home/dt_server/device/{0}.json".format("type_count"),static_type_result)
#     scp_jsonfile_without_pwd(local_path, remote_path, remote_ip, "type_count.json")
#     print(__file__,"----->OK")
#
# if __name__ == "__main__":
#     #file num : 40
#     local_path ="/home/dt_server"
#     #remote_path ="/home/mk_m/device"
#     remote_path ="/home/scp_test"
#     remote_ip ="45.77.11.167"
#     f_func()
#
#
#
#


