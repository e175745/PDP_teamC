import numpy as np
from modules import function
import time

if __name__ == "__main__":
    sum_list = []
    repeat_list = np.random.permutation(np.arange(1, 30001))
    start = time.time()
    num = 0
    while num < len(repeat_list):
        function.sum_from_one(num)
        num = num + 1
    
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
