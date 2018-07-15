#coding:utf-8
import os
def get_curdir():
    return os.getcwd()

#测试代码不能直接写，需要写在如下结果中
if __name__ =="__main__": #__nme__是python内置的1个专有变量
    print(os.getcwd())
    print(get_curdir())
