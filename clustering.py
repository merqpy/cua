from pickle import FALSE
from sys import flags
from telnetlib import PRAGMA_HEARTBEAT
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import numpy as np
def dbscan(x):
    clustering=DBSCAN(eps=0.03,min_samples=2).fit(x)
    print(clustering.labels_)

def kmean(x):
    clustering=KMeans(n_clusters=2,n_init=10).fit(x)
    return clustering.labels_

def cluster_flag(name,overturn):
    path_temp = r'C:\Users\28341\Desktop\Paper-Work\CuaGCL\test_embedding\embedding.txt'
    a=np.loadtxt(path_temp)
    label=kmean(a)
    print(label)
    flag=label
    file=r'C:\Users\28341\Desktop\Paper-Work\CuaGCL\test_embedding\flags.txt'
    fo=open(file,'w')  
    for i in range(len(flag)):
        fo.write(str(int(flag[i]))+'\n')

cluster_flag('MUTAG',False)

'''
for i in range(len(flag)):
    if(flag[i]==0):
        fo.write(str(int(flag[i])+1)+'\n')
    else:
        fo.write(str(int(flag[i])-1)+'\n')
'''




