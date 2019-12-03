import pandas as pd
import numpy as np

data = pd.read_csv('data1.csv', index_col='id')


def inf_div(u):
    n = u['count']  # count
    u = u.drop('count')
    u = u.drop('id')
    t = 0
    for i in u:
        if i != n and i != 0:
            t += n * np.log(n) - i * np.log(i) - (n - i) * np.log(n - i)
    return t


def inf_gain(a, b):
    c = a + b
    return inf_div(c) - inf_div(a) - inf_div(b)


def norm(x):
    y = [300, 189, 10, 50]
    # return np.sign(x - np.mean(x, axis=0)).add(1).divide(2)
    return np.sign(x - y).add(1).divide(2)


def add_v(d):
    arr = []
    for i, j in d.iterrows():
        q = int(''.join(map(str, j))[::-1], 2)
        arr.append(q)
    data['res'] = arr


def cluster(d):
    aa = []
    sum_aa = []

    for (method, group) in d.groupby('res'):
        group = group.drop('res', axis=1)
        summ = np.sum(group, axis=0)
        summ['count'] = len(group.index)
        summ['id'] = ' ' + str(method)
        sum_aa.append(summ)
        del summ
        aa.append(group)

    while len(sum_aa) != 1:
        min_aa = [inf_gain(sum_aa[0], sum_aa[1]), 0, 1]

        for i in range(len(sum_aa)):
            for j in range(i + 1, len(sum_aa)):
                if inf_gain(sum_aa[i], sum_aa[j]) < min_aa[0]:
                    min_aa[0] = inf_gain(sum_aa[i], sum_aa[j])
                    min_aa[1] = i
                    min_aa[2] = j

        sum_aa[min_aa[1]] = sum_aa[min_aa[1]] + sum_aa[min_aa[2]]
        sum_aa[min_aa[1]]['id'] = '(' + str(sum_aa[min_aa[1]]['id']) + ')'
        del sum_aa[min_aa[2]]
        print(sum_aa[min_aa[1]]['id'])


data = norm(data).apply(np.int64)
add_v(data)
cluster(data)
