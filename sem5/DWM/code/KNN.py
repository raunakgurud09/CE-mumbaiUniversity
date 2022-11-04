import pandas as pd 
import numpy as np 
import math 

df=pd.read_csv("KNN.csv") 
df.head() 
print(df, "\n")

x,y=3,7 
ls=[] 
for i,j in zip(df.X1,df.X2): 
    ls.append((math.dist([i,j],[x,y]))) 
ls 
print(ls, "\n")

df['Distance']=ls 
df.head() 
print(df, "\n")

df.sort_values('Distance',inplace=True) 
df.head() 
print(df, "\n")

df.reset_index(inplace= True) 
df.head() 
print(df, "\n")

k=3
ls1=[]
for i in range(k):
    ls1.append(df.Class[i])
ls1
print(ls1, "\n")

def most_frequent(List): 
    counter=0 
    num=List[0] 
    for i in List: 
        curr_frequency=List.count(i) 
        if(curr_frequency>counter): 
            counter=curr_frequency 
            num=i 
            return num 

print(most_frequent(ls1)) 