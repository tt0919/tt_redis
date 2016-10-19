#coding=utf-8
#操作顺序
#opera_redis-写0
#opera_redis_graph_dir
#redis_set_sip-写1
#redis_set_dip-写2
#ip_list-读库-1/2写库-3/4
#ip_bit-读库-0/3/4 写库-5/6
#bit_and
import redis
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=5)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=6)

ls_set=r_write_bit.keys('set*')
print ls_set