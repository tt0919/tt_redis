# -*- coding: utf-8 -*
#这种编程实现发现按照时间分窗口比按照包数分容易，和之前的编程方式不同
# bit偏移位从前往后数
import redis
import time
import networkx as nx
window_len = 1000

r_sip_list = redis.StrictRedis(host='localhost', port=6379, db=3)
r_dip_list = redis.StrictRedis(host='localhost', port=6379, db=4)
r_flow = redis.StrictRedis(host='localhost', port=6379, db=0)
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=5)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=6)

#r_write_inter = redis.StrictRedis(host='localhost', port=6379, db=7)

t = time.time()
count=1

ls_flow=r_flow.keys('*')
ls_set=r_write_set.keys('*')
ls_bit=r_write_bit.keys('*')
#le_inter=r_write_inter.keys('*')

#插入数据过程


for i in ls_flow:
    if(count%window_len<=window_len):
        temp_sip = "".join(r_flow.hmget('%s' % count, 'sip'))   # 从流中提取sip并重list转换成string
        temp_dip = "".join(r_flow.hmget('%s' % count, 'dip'))   # 从流中提取dip并重list转换成string
        sip = r_sip_list.get(temp_sip)  # 获取对应的哈希值
        dip = r_dip_list.get(temp_dip)
        # print sip
        wind=count/window_len
        r_write_set.sadd('set_sip_'+sip, 'bit_sip_'+sip+'_%s' % wind)   # 按照sip分类（如果想返回去查到sip地址则另外建立一个库）
        r_write_bit.setbit('bit_sip_'+sip+'_%s' % wind, dip, 1)     # bit位数组
        count += 1



#print 't1'
#计算交集过程
gra=[]
max=0
for i in ls_set:
    #print i
    for j in r_write_set.smembers(i):
        r_write_bit.bitop('and', i, j)
        print i
        print j
#print  r_write_bit.keys('*')
        #gra.append(j)
        #print gra
        #if(r_write_bit.bitcount(j)>max):
            #max=r_write_bit.bitcount(j)
            #print max
        #print i
        #print j

#print r_write_bit.getbit('sip_1',7)
#print r_write_bit.getbit('sip_2',7)
#print 't2'
#print r_write_bit.keys('*')
"""
#每个集合中的个数
for i in ls_set:
    print i
    print r_write_set.smembers(i)
#每个数组中个数
for i in ls_bit:
    print i
    print r_write_bit.bitcount(i)

"""
print time.time() - t

"""
import matplotlib.pyplot as plt                 #导入科学绘图的matplotlib包
#degree =  nx.degree_histogram(G)          #返回图中所有节点的度分布序列
x = range(max)                             #生成x轴序列，从1到最大度
y = range(max)
#将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
plt.show()
"""