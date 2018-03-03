#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:13:52 2018

@author: chiranjivibhatttarai
"""

import random
def random_walk(n):
    """
    Return co-ordinate after n block of random walk
    """
    x,y=0,0
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x+=dx
        y+=dy
        
    return (x,y)
#for i in range(25):
#    walk=random_walk(10)
#    print( walk, "distance from home=",abs(walk[0])+abs(walk[1]))

number_of_walks=10000
for walk_lenght in range(1,31):
    no_transport=0 # number of walks 4
    for i in range(number_of_walks):
        (x,y)=random_walk(walk_lenght)
        distance=abs(x)+abs(y)
        if distance<=4:
            no_transport+=1
    no_transport_percentage=float(no_transport)/number_of_walks
    print "walks size=",walk_lenght,"% of transport=",100*no_transport_percentage
    
