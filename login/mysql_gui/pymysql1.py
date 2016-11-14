#coding=utf-8
'''
Created on 2016年7月20日

@author: admin
'''
import pymysql
from readfile import readfile
class mysqlUp:
    def __init__(self,):
        tablist=readfile()
        self.values=[]
        for i in range(3):
            value=tuple(tablist[0])
            del tablist[0]
            self.values.append(value)
        self.pfdict=dict(tablist)
        self.ty=0
    def connexts(self):
        try:
            self.conn=pymysql.connect(host=self.pfdict["host"],
                                 port=int(self.pfdict['port']),
                                 user=self.pfdict['user'],
                                 passwd=self.pfdict['passwd'],
                                 db=self.pfdict['db'],
                                 charset=self.pfdict['charset'])
            
            self.cur=self.conn.cursor()      
        except:
            return ("连接数据库失败！")
        else:
            self.ty=1
            return ("连接数据库成功！")   
    def exeupdata(self):
        try:
            self.cur.executemany('update t_config_param set value=%s where name=%s',self.values)
            self.conn.commit()
        except Exception as e:
            self.quitnow()
            return ("数据库配置修改失败：%s" % e)
            
        else:
            return ('数据库配置修改完成！')
    def houseup(self):
        try:
            self.cur.execute('truncate table BD_WAREHOUSE_INFO;')          
            self.cur.execute(self.pfdict["sql"])
            self.cur.execute('select warehouse_id from bd_warehouse_info;')
            data=self.cur.fetchone()[0]
            self.cur.execute("update CLIENT_APP_INIT_DOLIST set WAREHOUSE_ID = '%s',IS_SYN = 0;" % data)
            self.cur.execute("UPDATE CLIENT_APP_CONFIG_CONDITION set ACC_CONDITION = '%s' WHERE ACC_CODE='WH_ID';" % data)
            self.cur.execute("UPDATE BA_LABEL_DOWNLOAD_CONFIG set WAREHOUSE_ID = '%s';" % data)
            
            self.cur.execute("update ef_sys_quartz_task set is_enable='0';")
            self.cur.execute("update ef_sys_quartz_task set is_enable='1' where JOB_NAME='synClientInitDataTask';")
            self.conn.commit()
        except Exception as e:
            self.quitnow()
            return ("仓库数据配置失败：%s" % e)
        else:
            return ("仓库数据配置完成！")
    def quitnow(self):
        try:
            self.cur.close()
            self.conn.close()
        except:
            pass
    def upsqlmain(self):
        self.connexts()
        self.exeupdata()
        self.houseup()
        self.quitnow()

if __name__=='__main__':
    sqlinfo=mysqlUp()
    con=sqlinfo.connexts()
    print con
    con=sqlinfo.houseup()
    print con
        
        
