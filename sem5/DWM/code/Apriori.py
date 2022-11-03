import numpy as np
import pandas as pd
from itertools import combinations

df = pd.read_csv('./Apriori Dataset.csv')
dff = pd.DataFrame(df)
di = dff.Items.str.split(',')

suppCount = int(input("Enter the minimum support count : "))
Confidence = int(input("Enter the minimum confidence : "))

print("DATASET:")
print(df)
print()

def validate(data, sc):
    data1 = pd.DataFrame()
    for i in range(len(data)):
        if data.iloc[i, 1] >= sc:
            temp = {'Itemsets': data.iloc[i, 0], 'supp_count': data.iloc[i, 1]}
            data1 = data1.append(temp, ignore_index=True)
    return data1

def combinations1(list_of_items):
    itemsets = []
    i = 1
    for entry in list_of_items:
        proceding_items = list_of_items[i:]
        for item in proceding_items:
            if (type(item) is str):
                if entry != item:
                    tuples = (entry, item)
                    itemsets.append(tuples)
            else:
                if entry[0:-1] == item[0:-1]:
                    tuples = entry + item[1:]
                    itemsets.append(tuples)
        i = i + 1
    if (len(itemsets) == 0):
        return None
    return itemsets

def count_itemsets(di, itemsets):
    count_itemset = {}
    for row in di:
        a = set(row)
        for itemset in itemsets:
            b = set(itemset)
            if (b.intersection(a)) == b:
                if itemset in count_itemset:
                    count_itemset[itemset] += 1
                else:
                    count_itemset[itemset] = 1
    data = pd.DataFrame()
    data['ItemSets'] = count_itemset.keys()
    data['supp_count'] = count_itemset.values()
    return data


# Obviously to print rules
def rules(Itemsets, Confidence):
    va = []  # if A->BC va is A
    vb = []  # if A->BC va is BC
    vc = []  # Confidence of above thingy
    # Above 3 only contain strong rules
    print("Rules : ")
    for l in Itemsets:
        l = frozenset(list(l))
        c = [frozenset(q) for q in combinations(l, len(l) - 1)]
        for a in c:
            # to split a set ABC into A->BC & BC->A
            b = l - a # b is The second part a is first part of arrow
            ab = l
            sab = 0  
            sa = 0  
            sb = 0 
            for q in di:
                temp = set(q)
                if (a.issubset(temp)):
                    sa += 1
                if b.issubset(temp):
                    sb += 1
                if (ab.issubset(temp)):
                    sab += 1

            temp = sab / sa * 100
            # temp BC->A
            print(list(a), "-->>", list(b), "Confidence : ", temp)

            temp1 = sab / sb * 100  # Formula for Confidence
            # temp1 A->BC
            print(list(b), "-->>", list(a), "Confidence : ", temp1)

            if temp >= Confidence:
                va.append(list(a))
                vb.append(list(b))
                vc.append(temp)

            if (temp1 >= Confidence):
                va.append(list(b))
                vb.append(list(a))
                vc.append(temp1)

    # Obviously to print strong rules
    print()
    print("Strong Rules : ")
    for i in range(len(va)):
        print(va[i], "-->>", vb[i], "Confidence : ", vc[i])


count_item = {}
for row in di:
    for i in range(len(row)):
        if (row[i] in count_item):
            count_item[row[i]] += 1
        else:
            count_item[row[i]] = 1


data = pd.DataFrame()
data['ItemSets'] = count_item.keys()
data['supp_count'] = count_item.values()


freq = pd.DataFrame()

while (len(data) != 0):
    data = validate(data, suppCount)

    if (len(data) > 1) or (len(data) == 1 and int(data.supp_count >= suppCount)):
        freq = data
    if (len(data) != 0):
        Itemsets = combinations1(data.Itemsets)
        data = count_itemsets(di, Itemsets)

    print()
    print("ItemSet ")
    print(freq)

print()
rules(freq.Itemsets, Confidence)
