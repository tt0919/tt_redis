# -*- coding: utf-8 -*
import redis
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
#说明：画持续连接的图--读库-1
r = redis.Redis(host='127.0.0.1',port=6379,db=1)
G = nx.Graph()
ls = r.keys('*')
count=0
t = time.time()
j=0
"""

for e in ls:
    #count=0
    for lt in r.smembers(e):
        G.add_edge(e, lt)
        #count+=1
    #print e
    #print str(j)+':'+str(count) #output degree for every pot
    #j+=1

#print count #output all degree =289 that is wrong
"""


t = time.time()
level1 = []
for e in ls:
    for lt in r.smembers(e):
        G.add_node(e)
        G.add_node(lt)
        level1.append(lt)
print len(level1)
print len(ls)
level2 = []
for i in level1:
    for l in r.smembers(i):
        if l in level1:
            G.add_edge(i, l)
            level2.append(l)

nums = 0
for i in ls:
    if r.smembers(i) in level2:
        nums += 1
        if nums < 700:
            for tt in r.smembers(i):
                G.add_edge(i, tt)
    else:
        break

degree=G.degree()
print len(degree)
node_colors = []

for k,v in degree.items():
    #else:
    if k in level2:
        node_colors.append('b')
    if k in level1:
        node_colors.append('r')
    else:
        node_colors.append('g')
print type(G)
community_list = list(nx.k_clique_communities(G, 100))
print community_list

pos=nx.spring_layout(G)
fig = plt.figure(figsize=(15, 10),facecolor='white')
nx.draw(G, pos, width=1, nodelist = degree.keys(), node_color=node_colors, node_size = [np.sqrt(v+1)*20 for v in (degree.values())])
print time.time() - t

plt.show()
print time.time() - t

print nx.degree_histogram(G)
degree =  nx.degree_histogram(G)
x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
plt.loglog(x,y,color="blue",linewidth=2)
plt.show()

