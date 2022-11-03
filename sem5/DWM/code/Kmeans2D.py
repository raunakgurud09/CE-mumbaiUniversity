import numpy as np 
import math 

dataset = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]] 

k = 3 
cluster1 = [] 
cluster2 = [] 
cluster3 = [] 
centroid1 = [2, 10] 
centroid2 = [5, 8] 
centroid3 = [1, 2] 
iteration = 0 

def kmeans(): 
    global centroid1, centroid2, centroid3, cluster1, cluster2, cluster3, iteration 
    iteration = iteration + 1 
    print("\nIteration ", iteration) 

    for i in range(0, len(dataset)): 
        a = abs(math.sqrt((pow(centroid1[0] - dataset[i][0], 2)) + 
                          (pow(centroid1[-1] - dataset[i][-1], 2)))) 
        b = abs(math.sqrt((pow(centroid2[0] - dataset[i][0], 2)) + 
                          (pow(centroid2[-1] - dataset[i][-1], 2)))) 
        c = abs(math.sqrt((pow(centroid3[0] - dataset[i][0], 2)) + 
                          (pow(centroid3[-1] - dataset[i][-1], 2)))) 
        print(a, b, c) 
        if a > b and c > b: 
            cluster2.append(dataset[i]) 
        elif c > a and b > a: 
            cluster1.append(dataset[i]) 
        else: 
            cluster3.append(dataset[i]) 
        print(cluster1, cluster2, cluster3) 
    listx1 = [] 
    listy1 = [] 

    for x, y in cluster1: 
        listx1.append(x) 
        listy1.append(y) 
    x1, y1 = listx1, listy1 

    listx2 = [] 
    listy2 = [] 
    for x, y in cluster2: 
        listx2.append(x) 
        listy2.append(y) 
    x2, y2 = listx2, listy2 

    listx3 = [] 
    listy3 = [] 
    for x, y in cluster3: 
        listx3.append(x) 
        listy3.append(y) 
    x3, y3 = listx3, listy3 

    valx1 = sum(x1)/len(x1) 
    valy1 = sum(y1)/len(y1) 

    valx2 = sum(x2)/len(x2) 
    valy2 = sum(y2)/len(y2) 

    valx3 = sum(x3)/len(x3) 
    valy3 = sum(y3)/len(y3) 

    tup1 = (float("{:.2f}".format(valx1)), float("{:.2f}".format(valy1))) 
    tup2 = (float("{:.2f}".format(valx2)), float("{:.2f}".format(valy2))) 
    tup3 = (float("{:.2f}".format(valx3)), float("{:.2f}".format(valy3))) 

    print("\nThe mean centroids are \n", tup1, "\n", 
          tup2, "\n", tup3) 
    if tup1 == centroid1 and tup2 == centroid2 and tup3 == centroid3: 
        print("\nClusters have been formed") 
    else: 
        centroid1 = tup1 
        centroid2 = tup2 
        centroid3 = tup3 
        cluster1 = [] 
        cluster2 = [] 
        cluster3 = [] 
        kmeans() 

kmeans() 