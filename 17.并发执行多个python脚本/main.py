import multiprocessing
import time
import os





def fun1(num):
    os.system('python SBI_trust_daily_tb.py')
def fun2(num):
    os.system('python hki_stock_tb.py')
def fun3(num):
    os.system('python futures_tb.py')


def fun4(num):
    os.system('python nikki225_plus_jpx400_stock_tb.py')
def fun5(num):
    os.system('python sp500_stock_tb.py')
def fun6(num):
    os.system('python sbi_trust.py')

def fun7(num):
    os.system('python nasdap100_stock_tb.py')

def fun8(num):
    os.system('python main_index_tb.py')
# 1. 导入进程包
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=fun1, args=(5,))
    process2 = multiprocessing.Process(target=fun3, args=(5,))
    process3 = multiprocessing.Process(target=fun4, args=(5,))
    process4 = multiprocessing.Process(target=fun5, args=(5,))
    process5 = multiprocessing.Process(target=fun6, args=(5,))
    process6 = multiprocessing.Process(target=fun7, args=(5,))
    process8 = multiprocessing.Process(target=fun8, args=(5,))
    process7 = multiprocessing.Process(target=fun2, kwargs={'num':3}) # target

    #3. 启动进程
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()




