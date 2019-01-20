# -*- coding: utf-8 -*-

from inspect import getgeneratorstate
from collections import namedtuple

Event=namedtuple('Event','time proc action')


def taxi_process(ident,trips,start_time=0):

    time=yield Event(start_time,ident,'leave garage')
    for i in range(trips):
        time=yield Event(time,ident,'pick up passenger')
        time=yield Event(time,ident,'drop off passenger')

    yield Event(time,ident,'going home')



print (u'在命令行中，_变量绑定前一个结果')
'''
taxi=taxi_process(ident=13,trips=2,start_time=0)
>>> taxi
<generator object taxi_process at 0x018E81B0>
>>> next(taxi)
Event(time=0, proc=13, action='leave garae')
>>> taxi.send(_.time+7)
Event(time=7, proc=13, action='pick up passenger')
>>> taxi.send(_.time+29)
Event(time=36, proc=13, action='drop off passenger')
>>> taxi.send(_.time++5)
Event(time=41, proc=13, action='pick up passenger')
>>> taxi.send(_.time+95)
Event(time=136, proc=13, action='drop off passenger')
>>> taxi.send(_.time+0)
Event(time=136, proc=13, action='going home')
>>> taxi.send(_.time+0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

'''

import queue,random


print (u'这个示例要旨是说明如何在一个主循环中处理事件，以及如何通过发送数据驱动协程。这是asyncio包底层的基本思想')
class Simulator:

    def __init__(self,procs_map):

        self.events=queue.PriorityQueue()
        ##优先级队列，按时间正向排序
        self.procs=dict(procs_map)
        ##创建procs_map副本，不修改原

    def run(self,end_time):
        '''排定并显示事件，直到时间结束'''

        for _,proc in sorted(self.procs.items()):
            first_event=next(proc)
            self.events.put(first_event)
        ##将仿真事件依照时间正向排序并激活，放入events中

        sim_time=0
        ##将仿真钟归零

        while  sim_time < end_time:
            
            if self.events.empty():
                ##没有任务，break loop
                break

            current_event = self.events.get()
            ##获取优先级队列中time属性最小的Event对象

            sim_time,proc_id,previous_action = current_event
            print ('taxi:',proc_id,current_event)
            active_proc=self.procs[proc_id]

            # next_time=sim_time + compute_duration(previous_action)
            # 根据前一个动作，计算下一次活动的时间，本例中用下面的random.randint()函数代替
            next_time=sim_time + random.randint(5,30)

            try:
                next_event=active_proc.send(next_time)
                ##把计算得到的时间发送给出租车协程，协程会产出下一个时间，或者抛出StopIteration异常（完成时）

            except StopIteration:
                del self.procs[proc_id]
                ##如果抛出了StopIteration异常，从self.procs字典中删除那个协程
            else:
                ##没有抛出异常而执行

                self.events.put(next_event)
                ##把next_event放入队列中


        else:
            ##仿真系统由于到达结束时间而结束，而不是由于没有事件要处理而执行（while不是因为break，continue中断结束循环时执行）

            msg='*** end of simulation time: {} events pending ***'
            print (msg.format(self.events.qsize()))

taxi_num=3
DEPARTURE_INRERVAL=5
taxis={i:taxi_process(i,(i+1)*2,i*DEPARTURE_INRERVAL) for i in range(taxi_num)}
sim=Simulator(taxis)

print (u'''\
该离散事件仿真示例，说明如何使用生成器代替线程和回调，实现并发。
该系统虽然简单，但可以一窥事件驱动型框架（Tornado 和asyncio）的运作方式:在单线程中使用一个主循环驱动协程执行并发活动。
使用协程做面向事件编程时，协程会不断把控制权让步给主循环，激活并向前运行其他协程，从而执行各个并发活动。
这是一种协作式多任务，协程显示自主的把控制权让步给中央调度程序。
而多线程实现的是抢占式多任务，调度程序可以在任何时刻暂停线程，把控制权让步给其他线程。

        ''')


if __name__ =='__main__':

    sim=Simulator(taxis)
    sim.run(30)


    '''
    >>> sim.run(110)
    taxi: 0 Event(time=0, proc=0, action='leave garage')
    taxi: 1 Event(time=5, proc=1, action='leave garage')
    taxi: 2 Event(time=10, proc=2, action='leave garage')
    taxi: 1 Event(time=14, proc=1, action='pick up passenger')
    taxi: 2 Event(time=19, proc=2, action='pick up passenger')
    taxi: 0 Event(time=26, proc=0, action='pick up passenger')
    taxi: 1 Event(time=38, proc=1, action='drop off passenger')
    taxi: 2 Event(time=43, proc=2, action='drop off passenger')
    taxi: 0 Event(time=49, proc=0, action='drop off passenger')
    taxi: 1 Event(time=63, proc=1, action='pick up passenger')
    taxi: 2 Event(time=64, proc=2, action='pick up passenger')
    taxi: 0 Event(time=69, proc=0, action='pick up passenger')
    taxi: 2 Event(time=76, proc=2, action='drop off passenger')
    taxi: 1 Event(time=86, proc=1, action='drop off passenger')
    taxi: 0 Event(time=90, proc=0, action='drop off passenger')
    taxi: 1 Event(time=96, proc=1, action='pick up passenger')
    taxi: 1 Event(time=102, proc=1, action='drop off passenger')
    taxi: 2 Event(time=104, proc=2, action='pick up passenger')
    taxi: 0 Event(time=113, proc=0, action='going home')
    *** end of simulation time: 2 events pending ***

    '''

    print (u'可以看到协程的处理流程（逻辑）和多线程很想，但他是在一个线程中实现的，适合于IO密集型任务，不适合CPU密集型任务')

