# -*- coding: utf-8 -*-

import random,sys
from time import sleep,time
from concurrent import futures

MAX_WORKERS= 20

tl=[i*0.01 for i in range(20)]

def do_one(t=0.2):

    # print (t)
    sleep(t)
    return t


def do_many(tl=tl):

    workers=min(len(tl),MAX_WORKERS)
    
    with futures.ThreadPoolExecutor(workers) as executor:
        '''
        executor.__exit__()方法会调用executor.shutdown(wait=True)方法,它会在所有的线程都执行完毕前阻塞线程
        '''
        res=executor.map(do_one,tl)

    return len(list(res))
    ##返回获取结果的数量，如果有线程抛出异常，异常会在这里抛出，这与隐式调用next()函数从迭代器中回去相应的返回值一样


def main(do_many=do_many):

    t0=time()
    count=do_many()
    t=time()-t0
    msg='execute {:2d} task cost {:.2f} s'
    print (msg.format(count,t))

if __name__ =='__main__':
    main()






