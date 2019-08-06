import numpy as np
import time

start = time.time()
list = np.random.permutation(np.arange(1, 1000000001))
print(time.time() -start)
