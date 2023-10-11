# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:58:06 2021
@author: Arifur Rahaman
"""
#from math import sqrt
import math
def euclidean_distance(x, y):
    distance= 0.0
    length = len(x)
    for i in range(length):
        distance = distance + (x[i] - y[i])**2
    #return sqrt(distance)
    return math.sqrt(distance)
print(euclidean_distance([7,3], [7,7]))