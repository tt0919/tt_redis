# -*- coding: utf-8 -*
import redis
import time
#说明：读库-1/2写库-3/4
r_write_sip = redis.StrictRedis(host='localhost', port=6379, db=3)
r_write_dip = redis.StrictRedis(host='localhost', port=6379, db=4)
r_read_sip = redis.StrictRedis(host='localhost', port=6379, db=1)
r_read_dip = redis.StrictRedis(host='localhost', port=6379, db=2)

t = time.time()


ls_sip=r_read_sip.keys('*')
ls_dip=r_read_dip.keys('*')

count_sip=0
count_dip=0
for i in ls_sip:
        r_write_sip.set(i,count_sip)
        count_sip+=1
for i in ls_dip:
        r_write_dip.set(i,count_dip)
        count_dip+=1
print time.time() - t
