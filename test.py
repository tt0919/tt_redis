#coding=utf-8
import redis
r_write_set = redis.StrictRedis(host='localhost', port=6379, db=5)
r_write_bit = redis.StrictRedis(host='localhost', port=6379, db=6)

ls_set=r_write_bit.keys('set*')
print ls_set