# -*- coding: utf-8 -*-

from inspect import getgeneratorstate

from functools import wraps

def corotine(func):
    '''装饰器：向前执行到第一个yield表达式，预激func'''

    @wraps(func)
    def primer(*args,**kw):
        gen=func(*args,**kw)
        next(gen)
        return gen
    return primer

@corotine
def averager():
    '''coroute计算平均值'''

    total=0.0
    count=0
    average=None

    while True:

        term=yield average
        total+=term
        count+=1
        average=total/count

avg=averager()

print (u'可以看到averager已经被coroutine装饰器激活了')
print ('state:',getgeneratorstate(avg))
print ()


print (avg.send(1))
print ('state:',getgeneratorstate(avg))
print ()

print (avg.send(2))
print ('state:',getgeneratorstate(avg))
print ()

print (avg.send(3))
print ('state:',getgeneratorstate(avg))
print ()

print (u'close 可以关闭协程')
print (avg.close())
print ('state:',getgeneratorstate(avg))
print ()


print (u'使用yield from 句法调用协程时，会自动预激，因此，与coroutine装饰器不兼容')
print (u'python3.4标准库里的asyncio.coroutine装饰器不会预激协程，与yield from 兼容')