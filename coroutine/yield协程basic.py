# -*- coding: utf-8 -*-
import time

def func():

    while 1:
        print (u'coroutine started')
        x=yield
        print (u'coroutine received：%s'%x)
        yield x


f=func()
f.send(None) or next(f)
f.send(None)


def simple_coro2(a):

    print ('-> started: a=',a)
    b=yield a
    print ('-> received：b=',b)
    c=yield a+b
    print ('->received：c=',c)
    yield c

my_coro2=simple_coro2(5)
from inspect import getgeneratorstate
print ()
print (getgeneratorstate(my_coro2))
print ()

print (my_coro2.send(None))
print (getgeneratorstate(my_coro2))
print ()

print (my_coro2.send(18))
print (getgeneratorstate(my_coro2))
print ()

print (my_coro2.send(99))
print (getgeneratorstate(my_coro2))
print ()


next(my_coro2)
print (getgeneratorstate(my_coro2))
print ()

