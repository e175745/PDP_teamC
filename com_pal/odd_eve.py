from multiprocessing import Pool
import time
import numpy as np
import multiprocessing as mp
import multiprocessing as multi
L = 20000
total = 0
list = np.arange(1, 1000001)
proc = 2

#print(multi.cpu_count())
def subcalc(p): # p = 0,1,...,7
    subtotal = 0
    subtotal2 = 0
    # iの範囲を設定
    ini = len(list) * p / proc
    fin = len(list) * (p+1) / proc
    #print(ini)
    #print(fin)
    # 計算を実行
    for i in range(int(ini), int(fin)-int(len(list)/2)):
        subtotal += list[2*i]

    for i in range(int(ini), int(fin)-int(len(list)/2)):
        subtotal2 += list[2*i+1]


    return subtotal + subtotal2

if __name__ == '__main__':
    print(multi.cpu_count())
    pool = mp.Pool(proc)
    start = time.time()
    callback = pool.map(subcalc, range(proc))
    total = sum(callback)
    print (total)
    print(time.time()-start)
