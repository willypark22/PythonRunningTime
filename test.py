import math
import time
import sys
from math import sqrt
import re

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

def dist(p1, p2):
    return sqrt(pow(float(p1[0])-float(p2[0]),2) + pow(float(p1[1])-float(p2[1]),2))

def sort(points):
    less = []
    equal = []
    greater = []
    
    if len(points) > 1:
        pivot = points[0]
        for x in points:
            if x < pivot:
                less.append(x)
            if x == pivot: 
                equal.append(x)
            if x > pivot:
                greater.append(x)
            return sort(less)+equal+sort(greater)
            
    else: 
        return points
        

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points):
    sort(points)
    return nearest_neighbor_recursion(points)

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):
    min_distance = float("inf")
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            if dist(points[i], points[j]) < min_distance:
                min_distance = dist(points[i], points[j])
                
    return min_distance

def nearest_neighbor_recursion(points):
    min_distance = float("inf")
    mang0 = len(points)
    L = []
    R = []
    x = mang0/2
    #print x
    for i in range(0, x):
        L.append(points[i])
    if len(L) == 2:
        return dist(L[0], L[1])
    if len(L) == 1:
        return float("inf")
    #print L
    leftmin = nearest_neighbor_recursion(L)
    #print leftmin
    #leftmin = 9
    for j in range(x, mang0 - 1):
        R.append(points[j])
    if len(R) == 2:
        return dist(R[0], R[1])
    if len(R) == 1:
        return float("inf")    
    #print R
    #rightmin = 10
    rightmin = nearest_neighbor_recursion(R)
    #print rightmin
    if rightmin < leftmin:
        min_distance = rightmin
    else:
        min_distance = leftmin
    ChuDat = []
    for a in range(0, len(points)):
        Leffen = float(points[x][0]) - min_distance
        Fawful = float(points[a][0])
        already = False
        #print points[a]
        if Fawful >= Leffen:
            #print Fawful
            #print Leffen
            ChuDat.append(points[a])
            #print "yay"
            already = True
        #else:
            #print "no"
        Ice = float(points[x][0]) + min_distance
        if Fawful <= Ice:
            if not already:
                #print Fawful
                #print Ice
                ChuDat.append(points[a])
                #print "y2"
        #else:
            #print "no2"
    for b in range(0, len(ChuDat)):
        for c in range(b+1, len(ChuDat)):
            mayb = dist(ChuDat[b], ChuDat[c])
            if mayb < min_distance:
                min_distance = mayb
    #print ChuDat
    #print "ChuDat"   
    return min_distance

def read_file(filename):
    points=[]
    # File format
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
            x = point_match.group(1)
            y = point_match.group(2)
            points.append((x,y))
    #print(points)
    return points

def main(filename,algorithm):
    start_time = time.time()
    algorithm=algorithm[1:]
    points=read_file(filename)
    #print(algorithm)
    if algorithm =='c':
        print("Divide and Conquer: ", nearest_neighbor(points))
    if algorithm == 'f':
        print("Brute Force: ", brute_force_nearest_neighbor(points))
    if algorithm == 'oth':
        print("Divide and Conquer: ", nearest_neighbor(points))
        print("Brute Force: ", brute_force_nearest_neighbor(points))
        
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])