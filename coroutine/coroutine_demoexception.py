# -*- coding: utf-8 -*-

from inspect import getgeneratorstate

class DemoException(Exception):pass
'''演示用定义的异常'''

def demo_exc_handling():

    print ('->: coroutine start')
    while True:
        try:
            x=yield 
        except DemoException:
            print (u'DemoException handled. Continuing...')
        else:
            print('->:coroutine received:{!r}'.format(x))
    raise RuntimeError('This line should never run.')


exc_coro=demo_exc_handling()
next(exc_coro)

print (exc_coro.send(11))
print (getgeneratorstate(exc_coro))
print ()

print (u'throw DemoException')
print (exc_coro.throw(DemoException))
print (getgeneratorstate(exc_coro))
print ()

print (u'close coroutine')
print (exc_coro.close())
print (getgeneratorstate(exc_coro))
print ()


print (u'throw ZeroDivisionError!')
print (exc_coro.throw(ZeroDivisionError))

print ()



