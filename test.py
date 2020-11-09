import numpy as np
import random
#import controller
import copy
a = np.zeros((3, 4),dtype=np.int16) 
a[2,2]=2
a[1,2]=4
a[2,1]=2
a[2,0]=8
a[0,2]=4
b=np.where(a==2)
c = np.stack((b[0].T,b[1].T),axis=1)

print(a)
print(a.T) #after done use T again, this is up
print(np.flip(a,axis=1)) # after done flip it back, this is right
print(np.flip(a.T,axis=1))


f = copy.deepcopy(a)

print((a==f).all())

# if 0 in table: true
# else:
'''





'''
print(a[:,1][a[:,1]!=0])

d = np.array([[1,2,3],[3,4,5]],dtype=np.int16)
e = np.array([1,2],dtype=np.int16)
print((d == e))