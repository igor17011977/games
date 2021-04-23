import os
# import math
import numpy as np
from collections import Counter



# A = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [3, 1]]).tolist()
# print(A.count([0,1]))
#
# k=0
# m=[]
# z=0
# for i in A:
#     print(i)
#     if i[0]==k:
#         z=z+1
#     else:
#         m.append([k,z])
#         print(m)
#         k+=1
#         z=1
# print (m)

# A=[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
# I = np.array([True, True, False, True, False, False, False, False, False])
# print(I)
# print(lp[fill])

# a = np.array([1, 3, 0], float)
# b = np.array([0, 3, 2], float)
# c=a==b
# print (a[c])
# # print (lp)
# np.around([0.11, 0.19, 1.21, 1.28], decimals = 1)
#
#
# A  = np.array([[x, y] for x in range(10) for y in range(10)])
# A=A[:30]
# print (A)
#
# arr = np.random.randint(0, 100, (6, 6))
# print (arr)
#
# numbers = range(10)
# squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))

# coords = np.zeros((10, 10, 2))
# np.where(coords, x, y)

# print (coords)
#
# zx=np.array([[1,3],[2,5],[5,6],[6,7]])
#
#
#
# X = np.random.normal(loc=1, scale=10, size=(1000, 50))
# print (X)

# Z = np.full((len(zx), 2), [1, 2])
# print(Z)
# q=np.linalg.norm(zx-Z)
# print(q)
# i = np.where(zx == [2,5])
# print(i)
# a = np.arange(9)
# m=np.delete(a, 0)
# print(m)
# import logging
#

#
# AB = np.vstack((A, B))
# print (AB)
# a=[1,2,3,4,5,6,7,8,9]
# for i in a:print(i,i,sep="#")
# z=lambda x:a[x]+2
# print(z(2))
#

# zs=iter(a)
# print(zs.__next__())
# print(zs.__next__())
# z=[[i,j] for (i,j) in enumerate(a)]
# # print (a.__next__())
# for i in open("tet1.py"):
#     print (i,end='')
# print (b"\xD0\x98\xD0\xBD\xD1\x82\xD0\xB5\xD1\x80\xD0\xBD\xD0\xB5\xD1\x82-\xD0\xBC\xD0\xB0\xD0\xB3\xD0\xB0\xD0\xB7\xD0\xB8\xD0\xBD \xD0\xB6\xD0\xB5\xD0\xBD\xD1\x81\xD0\xBA\xD0\xBE\xD0\xB9 \xD0\xBE\xD0\xB4\xD0\xB5\xD0\xB6\xD0\xB4\xD1\x8B".decode('utf-8'))
all=set("dddgdfgd dgdfgd dgdgd dgdfg".split())

L = [1, [2, [3, 4] , 5], 6, [7, 8] ]
def sumtree(L):
    """
    lksjhgksjfgh;skjfgh;sfd
    kjbglskjfdghlskdjfghlksjfdg
    lkjfgakjdf[gqoeg;lad;fgldg;sdg
    ,jfhg;adfhg;ld;ksjhg;ksjhg;kd
    """

print(sumtree.__doc__)
# Анотация функции
def func(a1:"spam"=4, b1:(1,10)=5, c1:float=6)->int:
    print(a1)
    return a1 + b1 + c1
print(func(1,2)) #1+2 + 6
print(func.__annotations__)
vb=[[ 0,24], [ 0,25], [ 0,26], [ 0,27],[1,24],[ 2,23],[ 3,23],[ 3,28],[ 3,29],[ 4,24],[ 4,25],[ 8,29]]
# a5={1,1,2,3,4,5,5}
# print (a5)
vb1={*map(lambda x:x[0],vb)}
print (vb1)
z=list(vb1)
zx=z[len(z)//2]
print (zx)
# qwe=lambda x:x[1] if x[0]==zx else "a3"
# print
vb2={*map(lambda x:x[1] if x[zx:] else "a3", vb)}
vb2.discard("a3")
print (vb2)
# print (vb1[len(vb1)//2])

    # lp=[]
    # fg=[0]*4
    # print(fg)
    # l1 = np.array(fg)
    # l2 = np.array([11,22,33,44])
    # a = np.c_[l1, l2]

def gen () :

    for i in range(10) :

        X = yield i
        print(X)

G = gen()
next(G)
print (G.send(77))
print (G.send(88))

import timeit

#
# code_to_test = """
# a = range(100000)
# b = []
# for i in a:
#     b.append(i*2)
# """
#
# elapsed_time = timeit.timeit(code_to_test, number=1)
# print(elapsed_time)
#
# code_to_test = """
# lp=[[x, y] for x in range(500) for y in range(500)]
# """
# elapsed_time = timeit.timeit(code_to_test, number=1)
# print(elapsed_time)
#
# code_to_test = """
# line_w=list(map((lambda x:x), range(500)))
# for i in range(500):
#     line_h=[i]*500
#     a = numpy.c_[line_h, line_w]
#     lp1.extend(a.tolist())
# """
# elapsed_time = timeit.timeit(code_to_test, number=1)
# print(elapsed_time)
bn=[1,2,3,4]
nm=[1,2,3,4]
asq=zip(bn,nm)
print (bn+nm)