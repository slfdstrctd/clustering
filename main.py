import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', index_col='id')


def inf_div(u):
    n = u['count']  # count
    u = u.drop('count')
    t = 0
    for i in u:
        if i != n and i != 0:
            t += n * np.log(n) - i * np.log(i) - (n - i) * np.log(n - i)
    return t


def inf_gain(a, b):
    c = a + b
    return inf_div(c) - inf_div(a) - inf_div(b)


def norm(x):
    return np.sign(x - np.mean(x, axis=0)).add(1).divide(2)


def add_v(d):
    arr = []
    for i, j in d.iterrows():
        q = int(''.join(map(str, j))[::-1], 2)
        arr.append(q)

    data['res'] = arr


data = norm(data).apply(np.int64)

add_v(data)

aa = []
sum_aa = []

for (method, group) in data.groupby('res'):
    group = group.drop('res', axis=1)
    summ = np.sum(group, axis=0)
    summ['count'] = len(group.index)
    sum_aa.append(summ)
    aa.append(group)
print(sum_aa)

print(inf_gain(sum_aa[0], sum_aa[5]))