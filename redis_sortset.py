import redis
import time
#sys.path.append()
file=open('/program-file/tt/src/main/resources/pcapAnaly.txt','r')
#file=open('/Users/admin/Downloads/pcap_analysis-master/tt/src/main/resources/test1.txt','r')
r = redis.StrictRedis(host='localhost', port=6379, db=6)
done=0
count=1
t = time.time()
while not done:
        str=file.readline()
        if(str!=''):
                #print str
                str_split = str.split('~')
                r.sadd(str_split[0].strip('\n'), count,str_split[1].strip('\n'))
                count+=1
        else:
                done=1
print time.time() - t
file.close()
