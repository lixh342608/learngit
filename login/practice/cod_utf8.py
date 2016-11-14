#coding=utf-8
'''
Created on 2016年7月4日

@author: admin
'''
import chardet
def cod_utf8(text,target_cod="utf-8"):

    cod=chardet.detect(text)["encoding"]
    print cod
    if cod != None:
        if cod=="gb2312":
            cod="gbk"
        return text.decode(cod).encode(target_cod)
    else:
        return ""
if __name__=="__main__":
    text=cod_utf8("真心英雄")
    print text