# -*- coding: utf-8 -*
#import sys
#sys.path.append('/Redis/redis-2.6')
import redis
import time
#sys.path.append()
#file=open('D:/BaiduYunDownload/data/new/1-ddostrace.from-victim.20070804_134936.txt','r')
#print file.readline()
file=open('D:/program-file/tt/tt_pcap/src/main/resources/pcapAnaly.txt','r')
#说明：集合方式存储在库-1中--写库-1
r = redis.StrictRedis(host='localhost', port=6379, db=1)
done=0
t = time.time()
while not done:
        str=file.readline()
        if(str!=''):
                #print str
                str_split = str.split('~')
                #r.set(str_split[0].strip('\n'), str_split[1].strip('\n'))
                #print str_split[0].strip('\n')
                #print str_split[1].strip('\n')
                r.sadd(str_split[0].strip('\n'), str_split[1].strip('\n'))
        else:
                done=1
print time.time() - t

file.close()
