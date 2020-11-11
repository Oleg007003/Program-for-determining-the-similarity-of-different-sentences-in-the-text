import pandas as pd
import numpy as np
import re
import scipy as sp
import scipy.spatial.distance
f = open('dts.txt', 'r', encoding='utf8')
s = ''
cnt = 0
for line in f:
    s += line
    cnt += 1
s = s.lower()
s =  re.split('[^a-z]', s)
s = list(filter(None, s))
s = list(set(s))
matrix = np.ones((cnt,len(s)))
i = 0
f.close()
f = open('dts.txt', 'r', encoding='utf8')
for line in f:
    tmp = line.lower()
    tmp = re.split('[^a-z]', tmp)
    tmp = list(filter(None, tmp))
    for j in range(0, len(s)):
        matrix[i, j] = tmp.count(s[j])
    i += 1
f.close()
dists = []
for row in matrix:
    dists.append(sp.spatial.distance.cosine(matrix[0,:],row))
dists = dists[1:]
min_1 = min(dists) # Находим самое ближайшее предложение
min_1_ind = dists.index(min_1)
dists = dists[:min_1_ind] + dists[min_1_ind + 1:]
min_2 = min(dists) # А теперь второе по величине
print(min_2)
file = open('submission-1.txt', 'w')
file.write(str(min_1) + ' ' + str(min_2))
file.close()