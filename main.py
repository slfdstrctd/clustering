import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', index_col='id')


def inf_div(a):
    n = np.sum(a)
    t = 0

    for i in a:
        t += i * np.log(i)
    return n * np.log(n) - t


def inf_gain(a, b):
    c = a + b
    return np.round(inf_div(c) - inf_div(a) - inf_div(b))


def norm(x):
    return np.sign(x - np.mean(x, axis=0)).add(1).divide(2)


def add_v(d):
    a = []
    for i, j in d.iterrows():
        for k in j.iteritems():
            print(k)

# k = np.array([1, 3])
# p = np.array([17, 6])


print(add_v(norm(data)))
