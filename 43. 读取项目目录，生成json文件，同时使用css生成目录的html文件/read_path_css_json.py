import json
import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def tree_path_json(path):
    dir_structure = {}
    base_name = os.path.basename(os.path.realpath(path))
    if os.path.isdir(path):
        dir_structure[base_name] = [tree_path_json(os.path.join(path, file_name)) for file_name in os.listdir(path)]
    else:
        return os.path.basename(path)
    return dir_structure


# print(tree_path_json())


def use_selenium_textarea_json_css(json_content):
    # use selenium 输入 json的内容


    # 1,打开网址
    driver.get('https://www.json.cn/#')  # 打开有道翻译首页

    # 2,输入框输入内容
    e = driver.find_element(By.ID, 'json-src')
    e.send_keys(json_content)
    time.sleep(1)
    html = driver.page_source
    pattern_str = '<div class="ro" id="json-target"(.*?)<br style="clear:both;">'
    pattern = re.compile(pattern_str,re.S)
    items = re.findall(pattern,html)
    f_item = '<div class="ro" id="json-target"'+ items[0]
    return f_item


def writeinto_htmlfile(filename,data):
    with open(filename,"a",newline="",encoding="utf-8") as f:
        f.write(data)
        f.write("\n")





if __name__ =="__main__":
    path = "C:\\CSBook\\gin"
    path_info = tree_path_json(path)
    json_path_info = json.dumps(path_info)

    json_content = use_selenium_textarea_json_css(json_path_info)
    json_css = '<style type="text/css">.json_key{ color: #92278f;font-weight:bold;}.json_null{color: #f1592a;font-weight:bold;}.json_string{ color: #3ab54a;font-weight:bold;}.json_number{ color: #25aae2;font-weight:bold;}.json_boolean{ color: #f98280;font-weight:bold;}.json_link{ color: #61D2D6;font-weight:bold;}.json_array_brackets{}</style>'
    htmlname = path.replace("\\", "_").replace(":", "_") + ".html"
    json_title  = '<h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{0}</h2>'.format(htmlname)

    writeinto_htmlfile(htmlname, json_css)
    writeinto_htmlfile(htmlname, json_title)
    writeinto_htmlfile(htmlname, json_content)
    print("json_css--->",json_css)
    print("json_title--->",json_title)
    print("json_content--->",json_content)

