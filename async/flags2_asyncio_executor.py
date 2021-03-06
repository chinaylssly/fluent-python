# -*- coding: utf-8 -*-
import collections
import asyncio
import tqdm
from time import time,sleep

Result=collections.namedtuple('Result','time msg')

tl=[i for i in range(1,21)]


class DemoError(Exception):
    def __init__(self,code):
        self.code=code



@asyncio.coroutine
def do_one(t):
    ##单任务执行函数，抛出自定义测试的异常

    msg='function do_one get t:{:3d}'
    print (msg.format(t))

    if t % 2 ==0:
        '''NOTE: >>> 0.12 % 0.02=0.019999999999999993'''

        raise DemoError(code=2)
        

    elif t % 3 ==0:
        raise DemoError(code=3)

    else:
        yield from asyncio.sleep(t * 0.01)
        return t


def IO():
    ##模拟本地I/O

    with open(__file__,'r',encoding='utf-8')as f:

        r=f.read()
        # print (r)
        # print (u'where am I')
    
        ##不能sleep模拟IO，否则，造成loop已经close()





@asyncio.coroutine
def mid_do_one(t,semaphore,verbose):
    ##中间处理流程，限制并发数目
    '''
    semaphore参数是asyncio.Semaphore类的实例，Semaphore是同步装置，用于限制并发数量
    '''

    try:
        with (yield from semaphore):
            ##在yield from 表达式中把semaphore当做上下文管理器使用，防止阻塞整个系统，如果semaphore计数器的值是所允许的最大值，只有这个协程会阻塞

            t=yield from do_one(t)

    except Exception as exc:

        #raise x from y 链接原来的异常
        raise DemoError(exc.code) from exc

    else:
        msg=u'execute t={:3d} at mid_do_one'.format(t)
        loop=asyncio.get_event_loop()

        ##run_in_executor方法的第一个参数是Executor实例，如果设为None，使用时间循环的默认ThreadPoolExecutor实例
        loop.run_in_executor(None,IO,)
        ##IO时间很长的话，会导致loop已经关闭，无法成功执行IO操作

    if verbose and msg:
        print (msg)

    return Result(t,msg)


@asyncio.coroutine
def do_coro(tl,verbose,nums):
    ##这个协程的参数与flags_asyncio.py中do_many函数一样,但是不能直接调用

    counter=collections.Counter()

    #创建一个asyncio.Semaphore实例，最多允许激活nums个协程
    semaphore=asyncio.Semaphore(nums)

    #创建协程对象列表
    to_do=[mid_do_one(t,semaphore,verbose) for t in tl]

    ##获取一个迭代器，这个迭代器会在future运行结束后返回future
    to_do_iter=asyncio.as_completed(to_do)

    if not verbose:

        ##把迭代器传给tqdm函数，显示进度
        to_do_iter=tqdm.tqdm(to_do_iter,total=len(tl))

    for future in to_do_iter:

        try:
            ##获取asyncio.Future对象的结果，最简单的是调用yield from，而不是调用future.result()
            res=yield from future

        except DemoError as exc:

            code=exc.code
            try:
                ##尝试从原来的异常（__cause__）中获取异常信息
                error_msg=exc.__cause__.args[0]

            except IndexError:
                ##如果在原来的异常中找不到异常信息，异常的类名作为错误信息
                error_msg=exc.__cause__.__class__.__name__

            if verbose and error_msg:
                msg=u'*** Error for {}:{}'
                print (msg.format(code,error_msg))

        else:
            code=0

        counter[code]+=1

    return counter


def do_many(tl,verbose,nums):

    loop=asyncio.get_event_loop()
    coro=do_coro(tl=tl,verbose=verbose,nums=nums)
    counts=loop.run_until_complete(coro)

    loop.close()
    return counts



def main(do_many,*args):

    t0=time()
    result=do_many(*args)
    t=time()-t0
    msg='task cost {:.2f} s'
    print (msg.format(t))
    print (result)


if __name__=='__main__':

    # main(do_many,tl,False,50)
    main(do_many,tl,True,10)


            





 
