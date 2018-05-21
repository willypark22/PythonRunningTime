import argparse
import os
import sys
import time
import profile
import math
from math import sqrt
import re

#globa = 0

# Command line arguments
parser=argparse.ArgumentParser(description='Calculate the nearest two points on a plan')
parser.add_argument('--algorithm',default='a',\
    help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ruteforce only or (d)ivide and conquer only')
parser.add_argument('-v','--verbose',action='store_true')
parser.add_argument('--profile',action='store_true')
parser.add_argument('filename',metavar='<filename>',\
    help='Input dataset of points')
    
def sort(points):
    less = []
    equal = []
    great = []
    
    if len(points) > 1:
        pivot = points[0]
        for i in points:
            if i < pivot:
                less.append(i)
            if i == pivot: 
                equal.append(i)
            if i > pivot:
                great.append(i)
            return sort(less) + equal + sort(great)
    else: 
        return points

def findDist(p1, p2):
    a = pow(float(p1[0]) - float(p2[0]),2)
    b = pow(float(p1[1]) - float(p2[1]),2)
    return sqrt(a + b)

def nearest_neighbor(points):
    sort(points)
    return divideAndConquerNearestNeighbor(points)

#Divide and conquer version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def divideAndConquerNearestNeighbor(points):
    point1 = (-1, -1)
    point2 = (-1, -1)
    min_distance = float("inf")
    arraySize = len(points)
    left = []
    right = []
    middle = arraySize // 2
    for i in range(0, middle):
        left.append(points[i])
    if len(left) == 2:
        return findDist(left[0], left[1])
    if len(left) == 1:
        return float("inf")
    left_min = divideAndConquerNearestNeighbor(left)
    for j in range(middle, arraySize - 1):
        right.append(points[j])
    if len(right) == 2:
        return findDist(right[0], right[1])
    if len(right) == 1:
        return float("inf")    
    right_min = divideAndConquerNearestNeighbor(right)
    if right_min < left_min:
        min_distance = right_min
        #print(min_distance)
    else:
        min_distance = left_min
        #print(min_distance)
    currentPoints = []
    for a in range(0, len(points)):
        hi = float(points[middle][0])
        temp = float(points[a][0])
        Checking = False
        if temp >= hi:
            currentPoints.append(points[a])
            Checking = True
        ad = float(points[middle][0])
        if temp <= ad:
            if not Checking:
                currentPoints.append(points[a])
    for b in range(0, len(currentPoints)):
        for c in range(b + 1, len(currentPoints)):
            tempCheck = findDist(currentPoints[b], currentPoints[c])
            if tempCheck < min_distance:
                min_distance = tempCheck
                point1 = currentPoints[b]
                point2 = currentPoints[c]
    #print("Divide and Conquer algorithm is complete")
    return (min_distance)#, point1, point2)
#end def divide_and_conquer(points):

#Brute force version of the nearest neighbor algorithm
#Input: points := unsorted array of (x,y) coordinates 
#   [(x,y),(x,y),...,(x,y)]
#Output: tuple of smallest distance and coordinates (distance,(x1,y1),(x2,y2))
def bruteForceNearestNeighbor(points):
    min_distance = float("inf")
    point1 = (-1,-1)
    point2 = (-1,-1)
    #TODO: Complete this function
    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            if findDist(points[i], points[j]) < min_distance:
                min_distance = findDist(points[i], points[j])
                point1 = (points[i])
                point2 = (points[j])
    print("Brute force algorithm is complete")
    return (min_distance,point1,point2)
#end def brute_force_nearest_neighbor(points):

#Parse the input file
#Input: filename := string of the name of the test case
#Output: points := unsorted array of (x,y) coordinates
#   [(x,y),(x,y),...,(x,y)]
def parseFile(filename):
    points = []
    f = open(filename,'r') 
    lines = f.readlines()
    for line in lines:
        coordinate = line.split(' ')
        points.append((float(coordinate[0]),float(coordinate[1])))
    return points
#end def parse_file(filename):

#Main
#Input: filename  := string of the name of the test case
#       algorithm := flag for the algorithm to run, 'a': all 'b': brute force, 'd': d and c
def main(filename,algorithm):
    start_time = time.time()
    points = parseFile(filename)
    result = bruteForceResult = divideAndConquerResult = None
    if algorithm == 'a' or algorithm == 'b':
    #if algorithm == 'b':
        #TODO: Insert timing code here
        bruteForceResult = bruteForceNearestNeighbor(points)
        print(bruteForceResult)
        result = bruteForceResult
        print("Time: %s seconds" % (time.time() - start_time))
        with open(os.path.splitext(filename)[0]+'_distance.txt','w') as f:
            L = list(result)
            #fileNum = result[1] = result[2] = result[0]
            f.write(str(L[1]) + '\n')
            f.write(str(L[2]) + '\n')
            f.write(str(L[0]) + '\n')
    if algorithm == 'a' or algorithm == 'd':
    #if algorithm == 'd':    
        #TODO: Insert timing code here
        divideAndConquerResult = nearest_neighbor(points)
        print("Divide and Conquer algorithm is complete")
        print(divideAndConquerResult)
        result = divideAndConquerResult
        print("Time: %s seconds" % (time.time() - start_time))
        with open(os.path.splitext(filename)[0]+'_distance.txt','w') as f:
            #L = list(result)
            #fileNum = result[1] = result[2] = result[0]
            f.write(str(result))
    if algorithm == 'a': # Print whether the results are equal (check)
        if args.verbose:
            print('Brute force result: '+str(bruteForceResult))
            print('Divide and conquer result: '+str(divideAndConquerResult))
            print('Algorithms produce the same result? '+str(bruteForceResult == divideAndConquerResult))
            #print("Time: %s seconds" % (time.time() - start_time))
        result = bruteForceResult if bruteForceResult == divideAndConquerResult else ('Error','N/A','N/A')
    else:  
        result = bruteForceResult if bruteForceResult is not None else divideAndConquerResult
    #with open(os.path.splitext(filename)[0]+'_distance.txt','w') as f:
    #    L = list(result)
        #fileNum = result[1] = result[2] = result[0]
    #    f.write(str(L[1]) + '\n')
    #    f.write(str(L[2]) + '\n')
    #    f.write(str(L[0]) + '\n')
#end def main(filename,algorithm):

if __name__ == '__main__':
    args=parser.parse_args()
    main(args.filename,args.algorithm)
#end if __name__ == '__main__':
