#kMeans 2d
import math

dataset = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]] 

k = 3

#selected pt
centroid1 = [2, 10] 
centroid2 = [5, 8] 
centroid3 = [1, 2] 


cluster1 = []
cluster2 = []
cluster3 = []

itr = 0

def distance(pt1=[],pt2=[]):
    val = abs(math.sqrt((pow(pt1[0] - pt2[0], 2)) + (pow(pt1[-1] - pt2[-1], 2))))
    return val

def findMean(cluster=[]):

    print(cluster)
    listX = []
    listY = []
    for x,y in cluster:
        listX.append(x)
        listY.append(y)
    
    valX = sum(listX)/len(listX)
    valY = sum(listY)/len(listY)
    return [valX,valY]

def kMeans2d():

    global centroid1,centroid2,centroid3,cluster1,cluster2,cluster3,itr
    itr = itr +1

    for i in range(len(dataset)):
        a = distance(centroid1,dataset[i])
        b = distance(centroid2,dataset[i])
        c = distance(centroid3,dataset[i])

        if c > a and b > a:
            cluster1.append(dataset[i])
        elif c > b and a > b:
            cluster2.append(dataset[i])
        else:
            cluster3.append(dataset[i])
    print(cluster1,cluster2,cluster3)
    Tup1 = findMean(cluster1)
    Tup2 = findMean(cluster2)
    Tup3 = findMean(cluster3)

    meanTup1 = (float("{:.2f}".format(Tup1[0])), float("{:.2f}".format(Tup1[-1]))) 
    meanTup2 = (float("{:.2f}".format(Tup2[0])), float("{:.2f}".format(Tup2[-1]))) 
    meanTup3 = (float("{:.2f}".format(Tup3[0])), float("{:.2f}".format(Tup3[-1]))) 

    if centroid1 == meanTup1 and centroid2 == meanTup2 and centroid3 == meanTup3:
        print("\nClusters have been formed") 
        print(f"{meanTup1}\t{meanTup2}\t{meanTup3}")
    else: 
        centroid1 = meanTup1 
        centroid2 = meanTup2
        centroid3 = meanTup3
        cluster1 = [] 
        cluster2 = [] 
        cluster3 = [] 
        kMeans2d()

kMeans2d()



