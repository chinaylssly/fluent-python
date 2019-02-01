# _*_ coding:utf-8 _*_ 

class C:

    def __init__(self,):
        print (u'init C')
        self.a=5
        print (self.__dict__)


    def a(self,):
        print (u'call a')
        self.b=10
        print (self.__dict__)

    def b(self,):

        print (u'call b')
        self.a=self.__class__.a

        print (self.__dict__)

    @staticmethod
    def s():
        pass


def outter(cls,):
    from collections import OrderedDict

    for key,value in cls.__dict__.items():
        print (key,value)
        if  not key.startswith('__di') :
            value=(value.__class__,id(value))
            setattr(cls,key,value)




    return cls

C=outter(C)
print (C)
print (C.__dict__)

print (C.a)
import ctypes

print (C.a[1])

t1 = ctypes.cast(C.a[1], ctypes.py_object).value
print (t1)



t1=5
t1 = ctypes.cast(id(t1), ctypes.py_object).value

print (t1)



