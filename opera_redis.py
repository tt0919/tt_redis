# -*- coding: utf-8 -*
import redis
import time
#sys.path.append()
#file=open('D:/BaiduYunDownload/data/new/1-ddostrace.from-victim.20070804_134936.txt','r')
#说明：将从pcsp文件中提取出来的地址对按照哈希的方式存储在库-0中--写库-0
file=open('D:/program-file/tt/tt_pcap/src/main/resources/pcapAnaly.txt','r')
r = redis.StrictRedis(host='localhost', port=6379, db=0)
done=0
count=1
t = time.time()
while not done:
        str=file.readline()
        if(str!=''):
                #print str
                str_split = str.split('~')
                #r.set(str_split[0].strip('\n'), str_split[1].strip('\n'))
                r.hmset('%s'%count, {
                    'sip': str_split[0].strip('\n'),
                    'dip': str_split[1].strip('\n'),
                })
                #blog_info1 = r.hmget('%s'%count, 'sip', 'dip')
                #print blog_info1
                count+=1
        else:
                done=1
print time.time() - t
file.close()
