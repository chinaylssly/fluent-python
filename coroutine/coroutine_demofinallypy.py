# -*- coding: utf-8 -*-

from inspect import getgeneratorstate

class DemoException(Exception):pass
'''演示用定义的异常'''

def demo_exc_handling():

    print ('->: coroutine start')
    try:
        while True:
            try:
                x=yield 
            except DemoException:
                print (u'DemoException handled. Continuing...')
            else:
                print('->:coroutine received:{!r}'.format(x))
    finally:

        print (u'->: coroutine ending!')


print (u'NOTE: python3.3引入yield from结构的主要原因之一与把异常传入嵌套的协程有关。另一个原因是让协程更方便的返回值')
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




