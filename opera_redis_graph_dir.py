
import redis
import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np

r = redis.Redis(host='127.0.0.1',port=6379,db=1)
G = nx.Graph()
ls = r.keys('*')
arr1=[]
t = time.time()
for e in ls:
    for lt in r.hget(e,"sip"):
        G.add_edge(lt, r.hget(e,"dip"))
        arr1.append(e)

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


