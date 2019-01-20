# -*- coding: utf-8 -*-
import asyncio
import itertools
import sys


@asyncio.coroutine
#打算交给asyncio处理处理的协程要是有asyncio.coroutine装饰。这不是强制要求，但建议这样做
def spin(msg,):
    ##这里不需要spiner_thread.py中spin函数中用来关闭线程的signal参数

    write,flush = sys.stdout.write,sys.stdout.flush

    ##itertools.cycle函数会从制定的序列中反复不断地生成元素
    for char in itertools.cycle('|/-\\'):
        status=char + ' ' + msg
        write(status)
        flush()

        ##这是显示动画的诀窍，使用退格符\x08将光标移回来
        write('\x08' * len(status))

        try:
            yield from asyncio.sleep(0.1)
            #使用yield from asyncio.sleep(),这样的休眠不会阻塞事件循环

        except asyncio.CancelledError:
            #如果spin函数苏醒后抛出了asyncio.CancelledError异常，其原因是发出了取消请求，因此退出循环
            break

    ##使用空格清除状态消息，吧光标移回开头
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    #slow_function函数是协程，用休眠假装进行I/O操作，使用yield from继续执行事件循环

    yield from asyncio.sleep(3)
    return 42

@asyncio.coroutine
def supervisor():
    #supervisor()函数也是协程，因此可以使用yield from 驱动 slow_function

    spinner=asyncio.async(spin('thinking'))
    #asyncio.async(...)函数排定spin协程的运行时间，使用一个Task对象包装spin协程，并立即返回

    print ('spinner object:',spinner)

    #驱动slow_function()函数。结束后，获取返回值。同时事件循环继续运行，因为slow_function通过yield from asyncio.sleep(3)表达式将控制权交给了主循环
    result=yield from slow_function()

    #Task可以取消，取消后会在协程当前暂停的yield处抛出asyncio.CancelledError异常，协程可以捕获这个异常，也可以延迟取消，也可以拒绝取消
    spinner.cancel()
    return result
    

def main():

    #获取事件循环的引用
    loop=asyncio.get_event_loop()

    #驱动supervisor协程，让他运行完毕，这次协程的返回值是这次调用的返回值
    result=loop.run_until_complete(supervisor())
    loop.close()

    print ('Answer: ',result)



print (u'''
1、 asyncio.Task对象差不多与threading.Thread对象等效。Task对象像是实现协作式多任务库（如gevent）中的绿色线程（green thread）。
2、 Task对象用于驱动协程，Thread对象用于调用可调用对象
3、 Task对象不由自己动手实例化，而是通过把协程传给asyncio.async()函数或loop.create_task()方法获取
4、 获取的Task对象已经排定了运行时间（例如，由asyncio.async函数排定），Thread实例则必须调用start（），明确告知让它运行
5、 在线程版中，slow_function是普通函数，由线程调用。在异步版中，其实协程，有yield from 驱动
6、 没有API能从外部终止线程，因为线程可能随时中断，导致系统处于无效状态。如果想终止任务，可以使用Task.cancel()
7、 supervisor协程必须在man函数中由loop.run_until_complete方法执行
8、 线程必须记得保留锁，去保护程序中的重要部分，防止多步操作中断线程。协程会默认做好全方位保护，以防止中断d
    ''')
if __name__ =='__main__':

    main()

    r'''
    >>> main()
    spinner object: <Task pending coro=<spin() running at C:\Users\sunzhiming\Desktop\async\test.py:7>>
    Answer:  42
    >>>
    '''
