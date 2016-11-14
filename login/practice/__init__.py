#coding=utf-8
import subprocess,platform
from cod_utf8 import cod_utf8
from time import sleep


    

#print("测试网络连通")
def pingto(url="www.baidu.com",count=None):
    ostem=platform.system()
    #print ostem
    if ostem.lower()=="windows":
        cmd=["ping",url,"-t"]
    else:
        cmd=["ping",url]
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    sum=0
    while count==None or sum<=count:  
        buff = p.stdout.readline() 
        if buff == "" and p.poll() != None:
              continue
        else:
            print cod_utf8(buff)
            sum+=1
    
    p.terminate()
if __name__=="__main__":
    pingto(count=5)


