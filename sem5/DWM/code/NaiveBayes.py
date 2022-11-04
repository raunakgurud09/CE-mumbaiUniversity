import pandas as pd 
import numpy as np 

df=pd.read_csv("Naive.csv") 
df.head(10)
print(df, "\n")

df_obj1=pd.get_dummies(df['Stolen'],prefix="Stolen") 
print(df_obj1, "\n") 

df_obj2=pd.get_dummies(df,prefix=['Stolen','Color','Type','Origin'],columns=['Stolen','Color','Type','Origin']) 
print(df_obj2, "\n") 

prior_prob={} 
l1=df['Stolen'].unique() 
print(l1, "\n") 

l2=(df['Stolen'].value_counts()).tolist() 
print(l2, "\n") 

l3=[] 
for i in range(len(l2)): 
    l3.append((l2[i]/df.shape[0])) 
print(l3, "\n") 

prior_prob=dict(zip(l1,l3))
print(prior_prob, "\n") 

for (colname,colval) in df_obj2.iteritems(): 
    print(colname,colval.values, "\n") 

for (index,colname) in enumerate(df_obj2): 
    print(df_obj2[colname].values==df_obj2[colname].values) 