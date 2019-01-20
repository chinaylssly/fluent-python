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