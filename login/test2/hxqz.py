#coding=utf-8
'''
Created on 2015年12月30日

@author: admin
'''
import urllib,re,os
import hxxsxz
def geturl(url="http://www.huoxingwenxue.com/"):
    
    
    html=urllib.urlopen(url).read()
    #print html
    
    return html

def ppzz(html):
    listq=[]
    reg='<a href="(.+?)" class="book-name" title="(.+?)" target="_blank">'
    reg=re.compile(reg)
    reg=re.findall(reg,html)
    listq.append(reg)
    
    reg='<li><a href="(.+?)" target="_blank">(.+?)</a>-<a href=".+?" class="gray" target="_blank" rel="nofollow">.+?</a></li>'
    reg=re.compile(reg)
    reg=re.findall(reg,html)
    listq.append(reg)
    reg='<a href="(.+?)" title="(.+?)" target="_blank">'
    reg=re.compile(reg)
    reg=re.findall(reg,html)
    listq.append(reg)
    
    return listq


def ksxz(listq):
    for j in listq:
        for i in j:
            url='http://www.huoxingwenxue.com'+i[0]
            sname=i[1].replace(' ','')
            #print sname
            if os.path.isdir("d:\hxxs\%s" % sname.decode('utf-8')):
                pass
            else:
            
                os.mkdir("d:\hxxs\%s" % sname.decode('utf-8'))
            #break
        #break
            try:
                hxxsxz.running(url, sname)
            except:
                print "出问题了"
                continue
    
    


if __name__=='__main__':
    
    html=geturl()
    listq=ppzz(html)
    ksxz(listq)
    