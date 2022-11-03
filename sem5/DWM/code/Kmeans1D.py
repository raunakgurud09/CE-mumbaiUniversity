datas = {2,4,10,12,3,20,30,11,25}

# k = 2;
c1=2
c2=4
cluster1 =[]
cluster2=[]

meanCluster1 =0;
meanCluster2=0;
itr = 0

def distance(value,pt):
  dist = abs(value - pt)
  return dist;
  
def kCluster():
  
  global c1 , c2,cluster1 ,cluster2, itr
  itr = itr + 1

  for data in datas:
    if(distance(data,c1) <= distance(data,c2)):
      cluster1.append(data)
    else:
      cluster2.append(data)
      
  meanCluster1 = abs(sum(cluster1)/len(cluster1))
  meanCluster2 = abs(sum(cluster2)/len(cluster2))
      
  print('No.of iteration :', itr+ 1 ,'\n','New c1:',meanCluster1 , ' New c2:', meanCluster2,'\n')    
   
      
  
  if c1 == meanCluster1 and c2 == meanCluster2 :
    print( 'Cluster 1 :', cluster1,'\n Cluster 2 :', cluster2)
  else:
    c1=meanCluster1
    c2=meanCluster2
    cluster1 = []
    cluster2 = []
    kCluster()
    
  # print(itr)  
kCluster()
