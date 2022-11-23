

import datetime
import json
import time
import requests
import sys
from math import modf





class C():

    def __init__(self):
        self.status_list = []  # mng ctrl
        self.exec_mount_list = []

    def exex_fn(self,fn):
        if "ok" in self.status_list:
            sys.exit()
        else:
            fn()
    def request_fn(self,url,retry_max,retry_interval):
        while True:
            # 0--> 0.0 ,0.0-->0.0  ,1.0-->0.0
            int_num = modf(round(len(self.exec_mount_list) / retry_max, 2))[0]
            print(len(self.exec_mount_list))
            if len(self.exec_mount_list) > 0 and int_num == 0.0:
                time.sleep(retry_interval)
                print("-------------sleep 5 seconds-------------")
            self.exec_mount_list.append("exec_mount")
            response = requests.get(url)
            print(datetime.datetime.now())
            print(response.text)
            response_msg = json.loads(response.text)["msg"]
            if response_msg != "lock msg":
                result = response.text
                self.status_list.append("ok")
                return result
            else:
                continue



if __name__ == "__main__":
    url = ""
    f = C()
    f.request_fn(url,2,5)
    # print(res)
