from multiprocessing import Pool
import time
import numpy as np
import multiprocessing as mp
import multiprocessing as multi
import threading
import threading
from concurrent.futures import ThreadPoolExecutor
import queue

list = []
L = 20000
total = 0
list = np.random.permutation(np.arange(1, 1000000001))
proc = 4

#print(multi.cpu_count())
def subcalc(p, q): # p = 0,1,...,7
    subtotal = 0

    # iの範囲を設定
    ini = len(list) * p / proc
    fin = len(list) * (p+1) / proc
    #print(ini)
    #print(fin)
    # 計算を実行
    for i in range(int(ini), int(fin)):
        subtotal += list[i]

    q.put(subtotal)
    return subtotal



def main():
    q = queue.Queue()
    total = 0
    for i in range(proc):
        th = threading.Thread(target=subcalc, args=(i, q))
        th.start()
        th.join()
        total += q.get()


    return total


if __name__ == '__main__':
    start = time.time()
    print(main())
    print(time.time() -start)
