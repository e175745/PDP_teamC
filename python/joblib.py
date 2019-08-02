from joblib import Parallel, delayed
import numpy as np
from modules import function
import time

if __name__ == "__main__":

    repeat_list = np.random.permutation(np.arange(1, 100001))
    start = time.time()
    r = Parallel(n_jobs=-1)([delayed(function.sum_from_one)(i) for i in repeat_list])

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
