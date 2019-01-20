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
    for r in res:
        print (r)
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

    r'''
    prepare execute:0.02
    prepare execute:0.01
    prepare execute:0.00
    prepare execute:0.03
    prepare execute:0.04
    <Task finished coro=<do_one() done, defined at C:\Users\sunzhiming\Desktop\async\flags_asyncio.py:11> result=0.0>
    <Task finished coro=<do_one() done, defined at C:\Users\sunzhiming\Desktop\async\flags_asyncio.py:11> result=0.03>
    <Task finished coro=<do_one() done, defined at C:\Users\sunzhiming\Desktop\async\flags_asyncio.py:11> result=0.04>
    <Task finished coro=<do_one() done, defined at C:\Users\sunzhiming\Desktop\async\flags_asyncio.py:11> result=0.02>
    <Task finished coro=<do_one() done, defined at C:\Users\sunzhiming\Desktop\async\flags_asyncio.py:11> result=0.01>
    execute  5 task cost 0.06 s
    '''

    print (u'可以看到协程执行顺序并不按照tl的顺序执行')





