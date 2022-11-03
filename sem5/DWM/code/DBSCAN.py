from math import dist

p = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
leng = len(p)
l = [[] for i in range(leng)]

for i in range(leng):
    for j in range(leng):
        l[i].append(dist(p[i], p[j]))

min = int(input("Minimum No. of neighbouring pts:"))
e =  int(input("Minimum Dist e:"))
c = [0] * leng

for x in range(leng):
    for y in range(leng):
        if l[x][y] <= e:
            c[y] += 1

for i in range(len(c)):
    if c[i] >= min:
        print(f"{p[i]}: Core")
    elif 1 < c[i] < min:
        print(f"{p[i]}: Border")
    else:
        print(f"{p[i]}: Noise")
