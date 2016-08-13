# -*- coding: utf-8 -*
#这种编程实现发现按照时间分窗口比按照包数分容易，和之前的编程方式不同
import redis
import time
window_len=5000

r_sip_list = redis.StrictRedis(host='localhost', port=6379, db=3)
r_dip_list = redis.StrictRedis(host='localhost', port=6379, db=4)
r_flow = redis.StrictRedis(host='localhost', port=6379, db=0)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=5)
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=6)
r_write_inter = redis.StrictRedis(host='localhost', port=6379, db=7)

t = time.time()
count=1

ls_flow=r_flow.keys('*')
ls_set=r_write_set.keys('*')
ls_bit=r_write_bit.keys('*')
le_inter=r_write_inter.keys('*')

for i in ls_flow:
    if(count%window_len<=window_len):
        temp_sip = "".join(r_flow.hmget('%s' % count, 'sip'))   #从流中提取sip并重list转换成string
        temp_dip = "".join(r_flow.hmget('%s' % count, 'dip'))   #从流中提取dip并重list转换成string
        sip = r_sip_list.get(temp_sip)  #获取对应的哈希值
        dip = r_dip_list.get(temp_dip)
        #print sip
        wind=count/window_len
        r_write_set.sadd('sip_'+sip, 'sip_'+sip+'_%s' % wind)   #按照sip分类（如果想返回去查到sip地址则另外建立一个库）
        r_write_bit.setbit('sip_'+sip+'_%s' % wind, dip, 1) #bit位数组
        count += 1

for i in ls_set:
    for j in ls_bit:
        r_write_inter.bitop('and',i,r_write_set.smembers(i))


#每个集合中的个数
for i in ls_set:
    print i
    print r_write_set.smembers(i)
#每个数组中个数
for i in ls_bit:
    print i
    print r_write_bit.bitcount(i)

# 每个交集结果
for i in le_inter:
    print i
    print r_write_inter.bitcount(i)

print time.time() - t

"""
blog_info1 = r_flow.hmget('%s' % count, 'sip', 'dip')
        sip = r_sip_list.get(r_flow.hmget('%s' % count, 'sip'))
        print r_sip_list.get('192.168.210.147')
        print len('192.168.210.147')
        dip = r_dip_list.get(r_flow.hmget('%s' % count, 'dip'))
        print r_flow.hmget('%s' % count, 'sip')
        print len(r_flow.hmget('%s' % count, 'sip'))
        print sip
        #print len(sip)
        print r_flow.hmget('%s' % count, 'dip')
        print dip
        print type('192.168.210.147')
        print type(r_flow.hmget('%s' % count, 'sip'))
        #r_write_bit.setbit(sip, dip, 1)  # 不需要初始化默认为零但是循环更新需要清零
        #print blog_info1
        count += 1
"""
