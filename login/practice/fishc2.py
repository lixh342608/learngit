#coding=utf-8
'''
Created on 2016年6月6日

@author: admin
'''
import time as t

class Mytime:
    def __init__(self):
        self.sta=0
        self.sto=0
        self.until=["年","月","日","时","分","秒"]
        self.prompt="还未开始计时！"
    def __str__(self,other):
        return self.prompt
    __repr__=__str__
    def __add__(self):
        self.prompt="总共运行了"
        self.result=[]
        for i in range(6):
            self.result.append(self.lasted[i]+other.lasted[i])
            if self.result[i]:
                self.prompt+=(str(self.result[i])+self.until[i])
        return self.prompt
        
    def start(self):
        if self.sta != 0:
            print("请先结束本次计时！")
        else:
            self.sta=t.time()
            self.prompt="计时中...."
            print("计时开始...")
    
    def stop(self):
        if self.sta == 0:
            print("请先开始计时器！")
        else:
            self.sto=t.time()
            self._clac()
            self.sta=self.sto=0
            print("计时结束")
    def _clac(self):
        self.prompt="本次共运行了"
        self.lasted=int(self.sto-self.sta)
        

        
        
            
            
        print self.prompt
        
if __name__=="__main__":
    t1=Mytime()
    t1.start()
    #t1.start()
    t.sleep(90)
    t1.stop()
    t2.start()
    t.sleep(20)
    
        
        
            

    