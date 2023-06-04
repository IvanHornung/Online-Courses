import numpy as np

a = np.array([1,2,3,4])
print(a)
# [1 2 3 4]

import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized version:" + str(toc-tic) + "ms")
# 1.5ms

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("For Loop:" + str(toc-tic) + "ms")
# 500 ms


# Vectorization uses GPU whereas for-loop uses CPU