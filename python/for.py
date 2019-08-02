import numpy as np
from modules import function
import time

if __name__ == "__main__":
    sum_list = []
    repeat_list = np.random.permutation(np.arange(1, 100001))
    start = time.time()
    for i in repeat_list:
        sum_list.append(function.sum_from_one(i))

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    
