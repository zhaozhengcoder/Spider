#coding:utf-8
import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
import re


SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1
# 使用 os.path.expanduser('~') 获取当前操作系统平台的当前用户根目录
HISTORY_PATH = os.path.expanduser('~') + os.sep + '.shiyanlou_shell_history'

def ls(args):
    if len(args)>0:
        print os.getcwd()

def cd(args):
    if len(args) > 0:
        os.chdir(args[0])
    else:
        os.chdir(os.getenv('HOME'))
    print os.getcwd()
    return SHELL_STATUS_RUN

def getenv(args):
    #print 'test : ',args
    if len(args) >0:
        print(os.getenv(args))

def exit():
    #TO-DO
    print ('exit')

def history():
    #TO-DO
    print ('history')

def cat(arg):
    #TO-DO
    print ('cat')
    

def display_cmd_prompt():
    user=getpass.getuser()
    hostname=socket.gethostname()
    cwd=os.getcwd()
    base_dir=os.path.basename(cwd)

    home_dir=os.path.expanduser('~')
    if cwd==home_dir:
        base_dir='~'
    #sys.stdout.write("[%s@%s %s]$ " % (user, hostname, base_dir))
    #改變顏色
    sys.stdout.write("[\033[1;33m%s\033[0;0m@%s \033[1;36m%s\033[0;0m] $ " % (user, hostname, base_dir))
    sys.stdout.flush()



#這部分使用啦正則表達式來處理
def getsplit(str):
    # 其实就是按空格符将命令与参数分开
    # 比如，'ls -l /home/shiyanlou' 划分之后就是
    # ['ls', '-l', '/home/shiyanlou']
    #res=re.split(r'\s',str)
    res=re.split(r'\s+',str)
    return res



def isgetenv(tokens):
    token=tokens[0]
    #print token
    if token.startswith('$'):
        getenv(token[1:])
        #print os.getenv(token[1:])
        return True
    else:
        return False

#構建一個字典 字典裏面的value，指的是函數，比如cd是cd函數
built_in_cmds = {}
built_in_cmds['cd']=cd
built_in_cmds['ls']=ls
built_in_cmds['cat']=cat
built_in_cmds['exit']=exit
built_in_cmds['history']=history


#to-do 這裏應該寫成一個循環 

#輸出
display_cmd_prompt()
#等待輸入
cmd=sys.stdin.readline()
#切分
cmd_tokens=getsplit(cmd)
#cmd_tokens=[ls -l]
#for c in cmd_tokens:
#    print c
#cmd_tokens=preprocess(cmd_tokens)
if isgetenv(cmd_tokens)==False:
    #print cmd_tokens[0]
    #print cmd_tokens[1]
    cmd_args=cmd_tokens[1:]
    #print cmd_args
    if cmd_tokens[0] in built_in_cmds:
        #print cmd_args
        built_in_cmds[cmd_tokens[0]](cmd_args)
