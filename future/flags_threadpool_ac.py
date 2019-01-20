# -*- coding: utf-8 -*-

import random,sys
from time import sleep,time
from concurrent import futures

MAX_WORKERS= 20

tl=[i*0.01 for i in range(20)]

def do_one(t=0.2):

    sleep(t)
    return t


def do_many(tl=tl):

    tl=tl[:5]

    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do=[]
        for t in tl:
            future=executor.submit(do_one,t)
            to_do.append(future)
            msg='Schduled for {:.2f}: {}'
            print (msg.format(t,future))

        results=[]
        for future in futures.as_completed(to_do):
            res=future.result()
            ##在本例中，调用future.result()方法绝不会阻塞，因为future由as_completed函数产出
            msg='{} result: {!r}'
            print (msg.format(future,res))
            results.append(res)

        return len(results)



    return len(list(res))


def main(do_many=do_many):

    t0=time()
    count=do_many()
    t=time()-t0
    msg='execute {:2d} task cost {:.2f} s'
    print (msg.format(count,t))


print (u'''
严格来说，多线程实现的并发脚本都不能并行下载。使用concurrent.futures库实现的示例受到GIL(GLobal Interpreter Lock，全局解释器锁)的限制。
多线程最好用来处理IO密集型任务（线程数一般根据程序需要确定），多进程一般用来处理CPu密集型任务（进程数一般等于CPu的核数）
''')
if __name__ =='__main__':
    
    main()

    '''
    >>> main()
    Schduled for 0.00: <Future at 0x1bed4d0 state=finished returned float>
    Schduled for 0.01: <Future at 0x1b73690 state=running>
    Schduled for 0.02: <Future at 0x1c40a30 state=running>
    Schduled for 0.03: <Future at 0x1c40990 state=pending>
    Schduled for 0.04: <Future at 0x1c40b50 state=pending>
    <Future at 0x1bed4d0 state=finished returned float> result: 0.0
    <Future at 0x1b73690 state=finished returned float> result: 0.01
    <Future at 0x1c40a30 state=finished returned float> result: 0.02
    <Future at 0x1c40990 state=finished returned float> result: 0.03
    <Future at 0x1c40b50 state=finished returned float> result: 0.04
    execute  5 task cost 0.06 s
    '''






