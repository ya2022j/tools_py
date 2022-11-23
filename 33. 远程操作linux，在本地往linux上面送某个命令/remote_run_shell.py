#
# 1、安装paramiko包
#
# pip3 install paramiko
#
#
# 2、代码详解
#
# 部署环境执行直接用os.popen
#
# 复制代码
# import os
# """
# 当前环境执行shell
# """
# def exeShell(reqdata):
#     print(reqdata)
#     tmp = os.popen(reqdata).readlines()
#     tmp = tmp[0].replace('\n', '')
#     return tmp
# 复制代码
# 远程环境执行用ssh
#
# 复制代码
# import paramiko
# """
# reqdata  ：执行语句
# hostname : ip
# username : 环境登录账号
# password ：环境登录密码
# """
# def exeShellSHH(reqdata ,hostname ,username ,password):
#     print(reqdata)
#
#     # 创建ssh对象
#     ssh = paramiko.SSHClient()
#     # 允许连接不在know_hosts文件中的主机
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     # 连接服务器
#     ssh.connect(hostname=hostname ,port=22 ,username=username ,password=password)
#     # 执行命令
#     stdin ,stdout ,stderr = ssh.exec_command(reqdata)
#
#     # 获取命令结果
#     result = stdout.read()
#     # 将types转为str
#     result = result.decode('UTF-8').replace('\n', '')
#
#     ssh.close()
#     return result
# 复制代码
# 判断执行的环境是否是部署环境
#
# 复制代码
# def isIplocal(ip):
#     shell = "ifconfig |grep eth0 -A 1|tail -n 1|awk -F ':' '{print $2}'|awk '{print $1}'"
#     iplocal = exeShell(shell)
#
#     if ip == iplocal:
#         return True
#     else:
#         return False
# 复制代码

# python远程执行Linux命令


# 于公钥密钥连接：
#
# 客户端文件名：id_rsa
#
# 服务端必须有文件名：authorized_keys(在用ssh-keygen时，必须制作一个authorized_keys,可以用ssh-copy-id来制作)




def use_privateKey_run_linux_cmd(private_key,serverIP,cmds):
    import paramiko

    private_key = paramiko.RSAKey.from_private_key_file(private_key)

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # # 连接服务器
    ssh.connect(hostname=serverIP, port=22, username='root', pkey=private_key)

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmds)
    # 获取命令结果
    result = stdout.read()
    print(result.decode('utf-8'))
    # 关闭连接
    ssh.close()


#  注意在web 服务器上专门把22端口打开才好会处理！---》ok 了

#


if __name__== "__main__":
    private_key ="167id_rsa"
    serverIP ="45.77.11.167"
    cmds = 'df > /home/ddd'
    use_privateKey_run_linux_cmd(private_key, serverIP, cmds)

