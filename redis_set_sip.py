#import sys
#sys.path.append('/Redis/redis-2.6')
import redis
import time
#sys.path.append()
file=open('/program-file/tt/tt_pcap/src/main/resources/pcapAnaly.txt','r')
#print file.readline()
#file=open('/Users/admin/Downloads/pcap_analysis-master/tt/src/main/resources/test1.txt','r')

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
