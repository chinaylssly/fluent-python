# -*- coding: utf-8 -*-
import asyncio
import itertools
import sys
import random
from time import sleep,time


tl=[i*0.01 for i in range(20)]

@asyncio.coroutine
def do_one(t=0.2):

    print (u'prepare execute:%.2f'%t)
    yield from asyncio.sleep(t)
    return t


def do_many(tl=tl):

    loop=asyncio.get_event_loop()
    to_do=[do_one(t) for t in tl]
    wait_coro=asyncio.wait(to_do)
    res, _=loop.run_until_complete(wait_coro)
    print (res)
    print (_)
    loop.close()
    return len(res)

def main(do_many=do_many):

    t0=time()
    count=do_many()
    t=time()-t0
    msg='execute {:2d} task cost {:.2f} s'
    print (msg.format(count,t))

if __name__ =='__main__':
    main()






