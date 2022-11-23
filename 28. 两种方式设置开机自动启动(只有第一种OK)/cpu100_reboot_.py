



# 补救措施

# 每10分钟检测一次，如果cpu超过100%就重启，但是重启后没法识别重启服务啊！
# 还是得分开啊！

# https://baijiahao.baidu.com/s?id=1722174560616569543&wfr=spider&for=pc
# 1、修改 /etc/rc.d/rc.local 文件方式
#
# /etc/rc.d/rc.local 用于用户自定义开机启动程序，因此可以往里写开机要执行的命令或脚本。
#
# 1、设置 rc.local 的可执行权限
# # chmod +x /etc/rc.d/rc.local
#
# 2、创建待执行的脚本，如下：
# # cat /home/test.sh
#  #!/bin/bash
#  echo "hello world" >> /home/out.txt
#  date >> /home/out.txt
#
# 3、设置脚本的可执行权限
# # chmod +x /home/test.sh
#
# 4、把脚本放到 /etc/rc.d/rc.local 尾部
# # cat /etc/rc.d/rc.local
#   ...
#  /home/test.sh
#
# 5、重启系统使之生效
# # reboot
#
# 6、查看日志文件判断脚本是否执行
# # cat /home/out.txt
# hello world
# Thu Dec 30 20:45:00 CST 2021



# 2、使用 crontab 方式
#
# crond 是 linux 下用来周期性的执行某种任务或等待处理某些事件的一个守护进程，与 windows 下的计划任务类似，当安装完成操作系统后，默认会安装此服务 工具，并且会自动启动 crond 进程，crond 进程每分钟会定期检查是否有要执行的任务，如果有要执行的任务，则自动执行该任务。
#
# 因此我们可以使用 crondtab 命令创建一个任务，让该任务在重启时进行执行。
#
# # crontab -e
# //进入编辑，输入如下行
# @reboot /home/test.sh
#
# //重启设备
# # reboot
#
# //查看日志
# # cat /home/out.txt
# hello world
# Thu Dec 30 21:09:03 CST 2021



# 3、使用 systemd 服务
#
# Systemd 服务是一种以 .service 结尾的单元（unit）配置文件，用于控制由 Systemd 控制或监视的进程。简单说，用于后台以守护进程（daemon）的形式运行程序。
#
# systmd service 文件一般放在/etc/systemd/system/文件夹中。
#
# 创建一个服务如下
#
# //在/etc/systemd/system/下创建一个服务，如下
# # vim ser.service
#
# //[Unit] 区块：启动顺序与依赖关系。
# [Unit]
# //Description字段给出当前服务的简单描述
# Description=Run a Custom Script at Startup
# After=default.target
#
# //Service区块定义如何启动当前服务
# [Service]
# //ExecStart字段：定义启动进程时执行的命令
# ExecStart=/home/test.sh
#
# //Install区块，定义如何安装这个配置文件，即怎样做到开机启动
# [Install]
# //WantedBy字段：表示该服务所在的 Target,Target的含义是服务组，表示一组服务
# WantedBy=default.target
#
#
# //更新服务配置文件，并使能服务
# # systemctl daemon-reload
# # systemctl enable ser.service
#
# //重启系统
# # reboot
# 有关 systemd 服务还有很多实用方式，本文知识做到抛砖引玉的作用，有兴趣的话可以自行研究这方面的知识。