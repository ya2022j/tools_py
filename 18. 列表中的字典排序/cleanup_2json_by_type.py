#! -*- coding:utf-8 -*-
import json
import os


def readjsonfile(filename):
    with open(filename, 'r', encoding='utf-8') as fw:
        s = json.load(fw)
        return s


def writeinto_jsonfile(filename, list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    device_path = os.path.join(os.getcwd(),"device")

    seen = set()
    only_list = []
    result = readjsonfile("nikki225_module.json") + readjsonfile("jpx400_module.json")
    for item in result:
        if item["code"] not in seen:
            only_list.append(item)
            seen.add(item["code"])
    type_dict = {}

    for  item  in only_list:
        if item["type"] not in type_dict:
            type_dict[item["type"]] = [item]
        else:
            type_dict[item["type"]].append(item)

    print(len(only_list))
    for k,v in type_dict.items():
        writeinto_jsonfile(os.path.join(device_path,"{0}.json".format(k)),v)

