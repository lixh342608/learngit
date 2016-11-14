#coding=utf-8
#import time
#import cod_utf8 as cod

def a():
    while True:
        print "a"
        yield
        print "c"
def b(c):
    c.next()
    print "b"
    c.next()
    
a=a()
b(a)


    



