#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql







def count_all_tables_nums(dbname):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='db',
                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("show tables")
    table_list = [tu for tu in cursor.fetchall()]
    db.close()

    for table in table_list:
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='db',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        sql = "select ID from {0}".format(table[""])

        # 获得Cursor对象
        cs1 = db.cursor()
        # 执行select语句，并返回受影响的行数：查询一条数据
        count = cs1.execute(sql)
        # 打印受影响的行数
        print(table[""], "查询到--%d--条数据:" % count)