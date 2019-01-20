# _*_ coding:utf-8 _*_ 

import keyword
from collections import abc

class FrozenJSON:
    ##把JSON数据集转化成嵌套的FrozenJSON对象，列表和简单类型的FrozenJSON对象

    def __init__(self,mapping):

        # self.__data=mapping

        self.__data={}
        for key,value in mapping.items():
            if keyword.iskeyword(key) or (not key.isidentifier()):
                ##处理无效的属性名(python关键字和有效的变量名)

                key=u'_%s'%(key)

            self.__data[key]=value



    def __getattr__(self,name):

        if hasattr(self.__data,name):
            ##如果name是实例属性__data的属性，那么返回那个属性。调用keys等方法就是通过这种方式处理的
            return getattr(self.__data,name)

        else:
            #否则，从self.__data中获取name键对应的元素，返回调用FrozenJSON.build()方法得到的结果
            # return FrozenJSON.build(self.__data[name])
            try:
                return FrozenJSON.build(self.__data[name])
            except KeyError as exc:
                raise AttributeError('%s object has no attribute "%s"'%(self.__class__.__name__,name))  from exc


    @classmethod
    def build(cls,obj):

        if isinstance(obj,abc.Mapping):
            ##如果obj是映射，那就构造一个FrozenJSON对象

            return cls(obj)

        elif isinstance(obj,abc.MutableSequence):
            #如果是MutableSquence对象，必然是列表，因此我们把obj中的每一个元素递归的传给.build()方法，构造一个列表

            return [cls.build(item) for item in obj]

        else:
            #既不是列表，也不是映射，原封不动的返回obj
            return obj
 


def test():

    d={'a':'aa','b':['bb','bbb'],'c':{'cc':'ccc'},'class':'metaclass'}
    dd=FrozenJSON(d)
    print (dd.a)
    print (dd.b)
    print (dd.c)
    print (dd.c.cc)
    print (dd._class)
    print (dd.e)

    '''
    Result:

    >>> d={'a':'aa','b':['bb','bbb'],'c':{'cc':'ccc'},'class':'metaclass',"2":4}
    >>> dd=FrozenJSON(d)
    >>> dd.a
    'aa'
    >>> dd.b
    ['bb', 'bbb']
    >>> dd.c
    <explore0.FrozenJSON object at 0x013450B0>
    >>> dd.c.cc
    'ccc'
    >>> dd.class
      File "<stdin>", line 1
        dd.class
               ^
    SyntaxError: invalid syntax
    >>> dd._class
    'metaclass'
    >>>

    '''




if __name__ == '__main__':
    test()

    '''
    NOTE:

    >>> d=dict(((key,i) for key in 'abc' for i in range(3)))
    >>> d
    {'a': 2, 'c': 2, 'b': 2}
    >>>


    '''

