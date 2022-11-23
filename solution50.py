# def kontr(loc):
#     su = 1
#     for i in range(len(str(loc)) - 1):
#         su *= int(str(loc)[i:i+2])
#         if su == 0 or loc < su:
#             return False
#     if loc == su:
#         return True
#     return False
#
#
# n = int(input())
# for _ in range(n):
#     l, r = map(int, input().split())
#     cou = 0
#     for i in range(max(10, l), r + 1):
#         if kontr(i):
#             cou += 1
#     print(cou)
import numpy as np

# list1 = [[1,2,3,4], [5, 6, 7,8]]
# list2 =  [[0.1,0.2, 0.3, 0.4],[0.5,0.6, 0.7, 0.8], [0.9, -0.1, -0.2, -0.3], [-0.4,-0.5, -0.6, -0.7]]
list1 = [[0], [1]]
list2 = [[0.1, 0.2], [0.3, 0.4]]
vtr1 = np.array(list1)
# output = [[2, 1], [5, 4]].[[3, 4], [7, 8]] = [[2*3+1*7, 2*4+1*8], [5*3+4*7, 5*4+4*8]] = [[13, 16], [43, 52]]
vtr2 = np.array(list2)

print("We create vector from a list 1:")
print(vtr1)
print("We create a vector from a list 2:")
print(vtr2)

vtr_product = vtr1.T.dot(vtr2)
print("Dot product of two vectors: ", vtr_product)
