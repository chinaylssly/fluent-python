# -*- coding: utf-8 -*-
import asyncio
import itertools
import sys
import random
from time import sleep,time


tl=[i*0.01 for i in range(5)]

@asyncio.coroutine
def do_one(t=0.2):

    print (u'prepare execute:%.2f'%t)

    ##利用asyncio.sleep模拟I/O等需要用到异步操作的场景
    yield from asyncio.sleep(t)
    return t


def do_many(tl=tl):

    loop=asyncio.get_event_loop()
    to_do=[do_one(t) for t in tl]

    #虽然函数名是wait，但他不是阻塞型函数。wait是一个协程，等传给它的所有协程运行完毕后结束，wait函数有两个关键字，如果设定了可能会返回未结束的future
    # wait_coro=asyncio.wait(to_do,timeout=0.11)
    wait_coro=asyncio.wait(to_do,)

    #执行事件循环，直到wait_coro运行结束。事件循环运行的过程中，这个脚本会在这里阻塞。
    #wait_coro运行结果返回一个元组，第一个元素是一系列结束的future，第二个参数是一系列未结束的future.（都是集合）
    res, _=loop.run_until_complete(wait_coro)
    for r in res:
        print (r)
    # print (_)
    loop.close()
    return len(res)



print (u'在协程编程中，涉及I/O操作的步骤需要由yield from交出控制权，然后asyncio.coroutine装饰')
print (u'可以看出，协程的速度比线程的速度还要快，对比flags_thread.py可以看出')
print (u'asyncio.wait(...)协程的参数是一个由future或协程构成的可迭代对象。wait会报各个协程包装进一个Task对象')

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






