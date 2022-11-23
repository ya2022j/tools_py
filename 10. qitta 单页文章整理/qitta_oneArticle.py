#! -*- utf-8 -*-
import copy
import re
import json
import time

import requests
from lxml import etree








def use_selenium_headless_getdt(url):
    res = requests.get(url)
    return res.text
    # driver.get(url)
    # time.sleep(1)
    # html = driver.page_source
    # return html





def list_null(list_content):
    if list_content !=[]:
        result = list_content
    else:
        result = ["null"]
    return result



def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


def writeintoTSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
def writeintoMD_file(filename,data):
    with open(filename,'a', encoding="utf-8") as f_output:
        f_output.write(data)
if __name__=="__main__":

    url_list = ["https://qiita.com/CyberFortress/items/9b95fa3ee0f82c90d62f"]


    for one_url in url_list:



        html = use_selenium_headless_getdt(one_url)
        pattern_text = re.compile('<div id="personal-public-article-body">(.*?)<div class="css-1yzj1fm">',re.S)
        text = re.findall(pattern_text,html)


        pattern_title = re.compile('<h1 class="css-188vyrl">(.*?)</h1>',re.S)
        title = re.findall(pattern_title,html)
        for item in text:
            writeintoMD_file("{0}.md".format(title[0]), item)










