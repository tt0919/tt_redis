# -*- coding: utf-8 -*
import redis
#说明：按位做交集--读库-5/6
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=5)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=6)

ls_bit_set=r_write_set.keys('set*')
ls_set_set=r_write_bit.keys('set*')
test=r_write_bit.keys('*')

def fun_var_args(farg, *args):
    r_write_bit.bitop('and',farg, *args)
    for value in args:
        print "another arg:", value


for i in ls_bit_set:
    l=list(r_write_set.smembers(i))
    #print l
    fun_var_args(i,*l)

print len(ls_bit_set)
print len(ls_set_set)

print len(test)

print "活跃度"
for i in ls_set_set:
    print r_write_bit.bitcount(i)

print "超流"
for i in test:
    print r_write_bit.bitcount(i)



