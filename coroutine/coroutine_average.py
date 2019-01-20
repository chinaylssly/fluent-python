# -*- coding: utf-8 -*-

from inspect import getgeneratorstate

def averager():
    '''coroutine计算平均值'''

    total=0.0
    count=0
    average=None

    while True:

        term=yield average
        total+=term
        count+=1
        average=total/count
    


avg=averager()

print (avg.send(None))
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


print (avg.close())
print ('state:',getgeneratorstate(avg))
print ()