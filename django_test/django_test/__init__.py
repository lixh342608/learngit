#coding=gbk
class animel(object):
    def __init__(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    def desk(self):
        print "%s会跳舞" % self.name
        
class dog(animel):
    def __init__(self,name):
        super(dog,self).__init__(name)
        self.height=11

if __name__=="__main__":
    d=dog("kiki")
    print "大家好，我是%s" % d.getName()
    print d.height
    d.desk()
    #print 291.65+301.99+1297.22+1505.56+137.73+9043.92+8541.14+18087.13+7596.92+10852.78+706.44
        

""""a=animel("烁烁")
print "大家好，我是%s" % a.getName()
a._animel__desk()"""
