#coding=utf-8
'''
Created on 2016年7月6日

@author: admin
'''
import threading as th
import time

it = [0]
lock=th.Lock()
def conmer(t):
    it[0]=it[0]+t
    it[0]=it[0]-t
def test(t):
    for i in xrange(10000):
        lock.acquire()
        try:
            conmer(t)
        finally:
            lock.release()
        
if __name__=="__main__":
    t1=th.Thread(target=test,args=(5,))
    t2=th.Thread(target=test,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print it
"""import threading,time
 
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        for i in xrange(8):
            print "I am %s run for %d" % (self.name,i)
            time.sleep(3)
        print "Thread:%s run over" % (self.name)
if __name__ == "__main__":
    for i in range(0, 5):
        my_thread = MyThread()
        my_thread.start()"""
    
    



