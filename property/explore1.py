# _*_ coding:utf-8 _*_ 

import keyword
from collections import abc
import json

class FrozenJSON:
    ##把JSON数据集转化成嵌套的FrozenJSON对象，列表和简单类型的FrozenJSON对象


    def __new__(cls,obj):
        ##__new__是类方法，第一个参数是类本身，余下的参数与__init__方法一样，只不过没有self

        if isinstance(obj,abc.Mapping):
            ##如果obj是映射，那就构造一个FrozenJSON对象

            ##默认的行为是委托给超类的__new__方法。这里调用的是object基类的__new__方法，把唯一的参数设为FrozenJSON
            return super().__new__(cls)

        elif isinstance(obj,abc.MutableSequence):
            #如果是MutableSquence对象，必然是列表，因此我们把obj中的每一个元素递归的传给.build()方法，构造一个列表

            return [cls(item) for item in obj]

        else:
            #既不是列表，也不是映射，原封不动的返回obj
            return obj
 


    def __init__(self,mapping):

        # self.__data=mapping

        self.__data={}
        for key,value in mapping.items():
            if keyword.iskeyword(key) or (not key.isidentifier()):
                ##处理无效的属性名(python关键字和有效的变量名)

                key=u'_%s'%(key)

            self.__data[key]=value


    def __str__(self,):
        ##修改__str__,使得FrozenJsON对象向用户更好的显示

        return '{}.__str__ : {}'.format(self.__class__.__name__,json.dumps(self.__data))
        return self.__data



    def __getattr__(self,name):

        if hasattr(self.__data,name):
            ##如果name是实例属性__data的属性，那么返回那个属性。调用keys等方法就是通过这种方式处理的
            return getattr(self.__data,name)

        else:
            #否则，从self.__data中获取name键对应的元素，返回调用FrozenJSON()方法得到的结果
            # return FrozenJSON.build(self.__data[name])
            try:
                ##这里之前调用的是FrozenJSon.build方法，现在只需要调用FrozenJSon的构造方法
                return FrozenJSON(self.__data[name])

            except KeyError as exc:
                raise AttributeError('%s object has no attribute "%s"'%(self.__class__.__name__,name))  from exc






def test():

    d={'a':'aa','b':['bb','bbb'],'c':{'cc':'ccc'},'class':'metaclass',"2":4}
    dd=FrozenJSON(d)
    print (dd.a)
    print (dd.b)
    print (dd.c)
    print (dd.c.cc)
    print (dd._class)
    print (dd._2)
    # print (dd.e)

  
print (u'__new__方法会返回其他类的实例，但不会调用__init__方法')



if __name__ == '__main__':

    test()
    '''
    Result:

    >>> d={'a':'aa','b':['bb','bbb'],'c':{'cc':'ccc'},'class':'metaclass',"2":4}
    >>> f=FrozenJSON(d)
    >>> f.a
    'aa'
    >>> f.b
    ['bb', 'bbb']
    >>> f.c
    <explore1.FrozenJSON object at 0x01B61550>
    >>> f.c.cc
    'ccc'
    >>> f._class
    'metaclass'
    >>> f._2
    4
    >>> f.e
    ......
    AttributeError: FrozenJSON object has no attribute "e"
    '''