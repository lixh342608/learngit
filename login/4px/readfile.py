#coding=utf-8
'''
Created on 2016年2月29日

@author: admin
'''
import csv

def readfile(csvfile="testtab.csv"):
    
    tablist=[]
    try:
        with open(csvfile,"r") as f:
            reader=csv.reader(f)
            for i in reader:
                tablist.append(i)
    except IOError as e:
        print ("文件不存在:%s" % e)
        return None 
    return tablist

if __name__=="__main__":
    condict=dict(readfile())
    print condict["connext"]
    




