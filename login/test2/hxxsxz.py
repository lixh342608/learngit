#coding=utf-8
'''
Created on 2015年12月30日

@author: admin
'''
import urllib,re,os

def openht(url):



    html=urllib.urlopen(url).read()


    return html

def geturl(html):
    reg='href="(.+?)" target="_blank" title="更新于：.+?">(.+?)</a></li>'
    reg=re.compile(reg)
    urllist=re.findall(reg,html)
    return urllist
def getxs(urllist,sname):
    for i in urllist:
        if os.path.exists("d:\hxxs\%s\%s.html" % (sname.decode('utf-8'),i[1].decode('utf-8'))):
            continue
        else:
            url='http://www.huoxingwenxue.com/'+i[0]
            wz=urllib.urlopen(url).read()
            #print wz
            #break
            
            reg='<div class="content">([\s\S]*)<p class="alert alert-info">'
            reg=re.compile(reg)
            reg=re.findall(reg,wz)
            #print reg
            #break
            wit=open("d:\hxxs\%s\%s.html" % (sname.decode('utf-8'),i[1].decode('utf-8')),'w')
            wit.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'+reg[0])
            wit.close()
            
        
    
    
    
def running(url="http://www.huoxingwenxue.com/b-2104/",sname="佛门小和尚"):
    html=openht(url)
    urllist=geturl(html)
    getxs(urllist,sname)
    
if __name__=="__main__":
    running()
    