#coding=utf-8
'''
Created on 2016年10月13日

@author: pc
'''
from tkMessageBox import *
masg="""公司初创
在1996年，随着客户数量的不
顺丰自有全货机
顺丰自有全货机
断增长和国内经济的蓬勃发展，顺丰将网点进一步扩大到广东省以外的城市。至2006年初，顺丰的速递服务网络已经覆盖国内20多个省及直辖市，101个地级市，包括香港、澳门及台湾，成为中国速递行业中民族品牌的佼佼者之一。
顺丰速运（集团）有限公司（以下简称顺丰）作为一家主要经营国际、国内快递业务的港资快递企业，为广大客户提供快速、准确、安全、经济、优质的专业快递服务。
顺丰以“成就客户，推动经济，发展民族速递业”为自己的使命，积极探索客户需求，不断推出新的服务项目，为客户的产品提供快速、安全的流通渠道。
为了向客户提供更便捷、更安全的服务，顺丰速运网络全部采用自建、自营的方式。经过十几年的发展，顺丰已经拥有6万多名员工和4000多台自有营运车辆，30多家一级分公司，2000多个自建的营业网点，服务网络覆盖20多个省、直辖市和香港、台湾地区，100多个地级市。
为给客户提供更优质的快递服务，顺丰仍然不断投入巨资加强公司的基础建设，提高设备和系统的科技含量，不断提升员工的业务技能、自身素质和服务意识，以最全的网络、最快的速度、最优的服务打造核心竞争优势，塑造“顺丰”这一优秀的民族品牌，立志成为“最值得信赖和尊重的速运公司”。
快递起步
1996年，顺丰开始涉足国内快递。
顺丰的快递是深港货运的"自然延伸"，最初的产品基本是深港件，需求增长很快，顺丰象一块海绵，疯狂吸收着快递市场无处不在的养分。一位最早加入顺丰团队的老业务员回忆说："那时候顺丰只有十几个人，大家围在王卫身边，同吃同住，每天唯一的任务就是跑市场。我们这些业务员都象疯了一样，每天早出晚归，骑着摩托车在大街小巷穿梭。"
很快，顺丰以顺德为起点，将网络的触角延伸至广东省以外，通过向长三角地区复制业务模式，进而扩张到华中、西南、华北。
在顺德之外，顺丰新建的快递网点多数采用合作和代理的方式。每建一个点，就注册一个新公司。这种形式和加盟类似，分公司归当地加盟商所有，互相连成一个网络。顺丰各地网点的负责人是公司的中坚力量，他们上缴一定数额的利润，多余的则留下。令人惊奇的是，直到2002年之前，顺丰一直都没有总部，只有一大批广州顺丰、中山顺丰这样的地方公司。
这种"自然延伸"式的扩张，靠的是自发的加盟。因此，顺丰形成的网络并不是有规划的，而是哪里有市场哪里就有网络。例如广东省，下属县城几乎每个都有顺丰的站点，而在经济发展程度较弱的省份，除了省会城市之外基本没有网点。
顺丰采取的方式与其他公司的加盟方式很像，只不过更松散些。比如，加盟是一种公司之间的商业行为，需要办理工商手续，加盟商们使用公司的统一标识，对外承揽生意。小老板们可以把货送到公司的集散中心来走货，但盈亏要自己负责。
由于是业务带动市场，而此时的市场又很容易做，顺丰便将全部精力放在了市场拓展上，甚至曾采用"人海战术"，期望达到广种多收的效果。
起初，顺丰在业务运作中采取了一种简单的承包方式，给业务员划片、划区，每人负责一块"责任田"。各个片区在负责人的带领下，从开拓到收获，逐渐丰饶起来。一位老业务员回忆说，当时很多业务员骑摩托车取送件，时常有人不幸遇到车祸，断胳膊断腿是常事。"顺丰是我们用生命换来的。"业务员拼命换回来的是不菲的收入。在2000年，顺丰在广东一些城市的业务员，已经有一大批月收入上万元的。在这种示范效应下，顺丰的网络拓张一路顺风满帆。"""
showinfo("提示", masg)


"""from tkFileDialog  import asksaveasfilename

filename=asksaveasfilename(initialfile="test.txt")
print filename
if filename:
    text="hello"
    with open(filename,"w") as f:
        f.write(text)"""




"""from xlrd import open_workbook
from xlutils.copy import copy
 
rb = open_workbook(u"C:/test/更新日志.xls")
 
#通过sheet_by_index()获取的sheet没有write()方法
#rs = rb.sheet_by_index(0)
 
wb = copy(rb)

#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
row = ws._Worksheet__rows.get(5)
cell = row._Row__cells.get(4)
print cell
#ws.write(5, 5, 'changed!')
 
#wb.save(u"C:/test/更新日志.xls")"""