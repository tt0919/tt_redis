# -*- coding: utf-8 -*
import redis
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=7)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=8)
rr = redis.StrictRedis(host='localhost', port=6379, db=9)
ls_set=r_write_set.keys('*')

def fun_var_args(farg, *args):
    r_write_bit.bitop('and',farg, *args)
    for value in args:
        print "another arg:", value


for i in ls_set:
    l=list(r_write_set.smembers(i))
    print l
    fun_var_args(i,*l)



"""
def func(i):
    def inner_func(j):
        #print r_write_set.smembers(i)
        r_write_bit.bitop('and', i, j)
    return inner_func

for i in ls_set:
    print i
    bb = func(i)
    print r_write_set.smembers(i)
    bb(r_write_set.smembers(i))
"""



"""
#这种编程实现发现按照时间分窗口比按照包数分容易，和之前的编程方式不同
import redis

r_sip = redis.StrictRedis(host='localhost', port=6379, db=7)
r_bit = redis.StrictRedis(host='localhost', port=6379, db=8)
# test
ls_sip=r_sip.keys('*')

print r_bit.keys('*')
for i in ls_sip:
    #print r_sip.smembers(i)
    #r_bit.bitop('or', i, r_sip.smembers(i))
    for j in r_sip.smembers(i):
        #print r_bit.get(j)
        #print bin(eval("0x56"))
        print r_bit.getbit(j,1)
        print r_bit.getbit(j,3)
        r_bit.get



# r_bit.bitop('and','sip', 'sip_1','sip_2')

"""
