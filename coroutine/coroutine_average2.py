# -*- coding: utf-8 -*-

from inspect import getgeneratorstate
from collections import namedtuple

Result=namedtuple('Result','count average')

def averager():
    '''coroutine计算平均值'''

    total=0.0
    count=0
    average=None

    while True:

        term=yield 

        if term is None:
            break

        total+=term
        count+=1
        average=total/count

    return Result(count,average)
    


avg=averager()
avg.send(None)
avg.send(10)
avg.send(30)
try:

    avg.send(None)
except StopIteration as exc:

    result=exc.value

print (result)

print (u'该协程通过send(None)跳出循环，进而获取程序的返回值！！！')