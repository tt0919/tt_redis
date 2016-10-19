# -*- coding: utf-8 -*
import redis
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
#说明：将从库-0中地址对直接画图--读库-0
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
G = nx.Graph()
ls = r.keys('*')
arr1 = []
t = time.time()
count = 0
for e in ls:
    #count = 0
    for lt in r.hget(e,"sip"):
        #G.add_edge(lt, r.hget(e,"dip"))
        G.add_edge("root", lt)
        G.add_edge(lt,count)
        count = count + 1
        print count
        arr1.append(e)
print len(ls) #12302
print type(ls) # <type 'list'>
print type(arr1) # <type 'list'>
print len(arr1)
#len(arr1)=171130
degree=G.degree()

print len(degree)
node_colors = []

for k,v in degree.items():
    if k in arr1:
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


"""
# -*- coding: utf-8 -*
# 画图结果怪异有待改进
import redis
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
#说明：将从库-0中地址对直接画图--读库-0
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
G = nx.Graph()
ls = r.keys('*')
arr1=[]
t = time.time()
for e in ls:
    for lt in r.hget(e,"sip"):
        G.add_edge(lt, r.hget(e,"dip"))
        arr1.append(e)
print len(arr1)
#len(arr1)=171130
degree=G.degree()
print len(degree)
node_colors = []

for k,v in degree.items():
    if k in arr1:
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

"""
