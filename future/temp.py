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

if __name__ =='__main__':
    main()






