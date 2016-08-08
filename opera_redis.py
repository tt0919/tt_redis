import redis
import time
#sys.path.append()
file=open('/program-file/tt/src/main/resources/pcapAnaly.txt','r')
#file=open('/Users/admin/Downloads/pcap_analysis-master/tt/src/main/resources/test1.txt','r')
r = redis.StrictRedis(host='localhost', port=6379, db=5)
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
