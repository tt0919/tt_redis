#import matplotlib.pyplot as plt
#plt.bar(left=(0, 1), height=(1, 0.5))
#plt.show()
import sys
sys.path.append('/Users/admin/data')


import redis
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np

r = redis.Redis(host='127.0.0.1',port=6379,db=6)
G = nx.Graph()
ls = r.keys('*')
#roots = ['0.0.0.0']
#G.add_nodes_from(roots)
t = time.time()
level1 = []
for e in ls:
    #if r.smembers(e) in roots:
        #print r.smembers(e)
    for lt in r.smembers(e):
	    G.add_edge(e, lt)
	    level1.append(e)
print len(level1)
level2 = []
for i in ls:
    for l in r.smembers(i):
        if l in level1:
	    G.add_edge(i, l)
	    level2.append(i)

nums = 0
for i in ls:
    if r.smembers(i) in level2:
        nums += 1
        if nums < 700:
            for tt in r.smembers(i):
                G.add_edge(i, tt)
	else:
	    break
"""
for u in ls:
    if r.get(i) in level2:
    	G.add_edge(u, r.get(u))
"""
degree=G.degree()
print len(degree)
node_colors = []

for k,v in degree.items():
#    if k == 'Oralsexer' or k == 'hyyssysys':
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
"""
G.add_nodes_from([3,4,5,6])
G.add_nodes_from(ls)
G.add_cycle([1,2,3,4])
G.add_edge(1,3)
G.add_edges_from([(3,5),(3,6),(6,7),(8,9),(1,2),(1,3),(1,4)])
"""
print time.time() - t
#nx.draw_random(g)
plt.show()
print time.time() - t



