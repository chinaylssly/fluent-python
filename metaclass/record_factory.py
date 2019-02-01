# _*_ coding:utf-8 _*_ 

def record_factory(cls_name,fild_names):

    try:
        fild_names=fild_names.replace(',',' ').split()
        #这里体现了鸭子类型，尝试在逗号处或空格处拆分field_names;如果失败，那么假定field_names本来就是可迭代对象，一个元素对于一个属性名

    except AttributeError:
        pass

    fild_names=tuple(fild_names)
    #使用属性名构造元祖，这将成为新建类的__slots__属性；此外，这么做还设定了拆包和字符串表示形式中各字段的顺序。

    def __init__(self,*args,**kw):
        #这个函数将成为新建类的__init__方法。参数有位置参数和关键词参数

        attrs=dict(zip(self.__slots__,args))
        attrs.update(kw)

        for name,value in attrs.items():

            setattr(self,name,value)

    def __iter__(self,):
        #实现__iter__函数，把类的实例变成可迭代对象

        for name in self.__slots__:
            yield getattr(self,name)


    def __repr__(self,):
        #迭代__slots__和self,实现更友好字符串表示形式。

        values=', '.join('{}:{!r}'.format(*i) for i in zip(self.__slots__,self))
        return '{}({})'.format(self.__class__.__name__,values)


    cls_attr=dict(__slots__=fild_names,
                  __init__=__init__,
                  __repr__=__repr__,
                  __iter__=__iter__,)
    #组件类属性字典

    return type(cls_name,(object,),cls_attr)
    ##调用type的构造方法，构建新类，然后将其返回。（可以看做是调用了type类的构造方法__new___及初始化方法__init__）


def test():


    Dog=record_factory('Dog','name,weight,owner')
    rex=Dog('Rex',30,'Bob','jan')
    alx=Dog('name',weight=12,owner='jam',name='aftername')
    ##关键词参数会覆盖非关键词参数，比如：第一个参数形参名为name，实参为'name'字符串，但是被关键词参数name='aftername'覆盖了，这与__init__的实现有关







print (u'我们本可以把__slots__类属性的名称改成其他值，不过要那样的话，就要实现__setattr__方法，为属性赋值时验证属性的名称，因为对于记录这样的类，我们希望属性\
始终是固定的那几个，而且顺序相同。__slots__属性的主要特点是节省内存，能处理数百万个实例，不过也有一些缺点。')

print ()
print (u'record_factory函数创建的类，其实例有个局限--不能序列化，即不能使用pickle模块的dump/load函数处理。这个示例是为了说明如何使用type类实现简单的需求。\
需要了解完整的解决方案，请分析collections.namedtuple函数的源代码。')

if __name__ =='__main__':

    test()

    '''

    >>> Dog=record_factory('','name,weight,owner')
    >>> Dog
    <class 'record_factory.'>

    >>> Dog=record_factory('Dog','name,weight,owner')
    >>> Dog
    <class 'record_factory.Dog'>

    >>> rex=Dog('jackson',15,'jessie')
    >>> rex
    Dog(name:'jackson', weight:15, owner:'jessie')

    >>> dog=Dog('dog',11)
    >>> dog
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:/Users/sunzhiming/Desktop/metaclass/record_factory.py", line 35, in __repr__
        values=', '.join('{}:{!r}'.format(*i) for i in zip(self.__slots__,self))
      File "C:/Users/sunzhiming/Desktop/metaclass/record_factory.py", line 35, in <genexpr>
        values=', '.join('{}:{!r}'.format(*i) for i in zip(self.__slots__,self))
      File "C:/Users/sunzhiming/Desktop/metaclass/record_factory.py", line 29, in __iter__
        yield getattr(self,name)
    AttributeError: owner
    ##没有传递owner参数，所以getattr(self,name)会抛出AttributeError异常

    >>> rex=Dog('jackson',15,'jessie',name='rex')
    >>> rex
    Dog(name:'rex', weight:15, owner:'jessie')
    ##关键字参数覆盖了固定参数name的值

    >>> iters=iter(Dog)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'type' object is not iterable
    ##iter特殊方法会调用超类的__iter__方法

    >>> iters=Dog.__iter__(Dog)
    >>> iters
    <generator object record_factory.<locals>.__iter__ at 0x01752CF0>
    >>> for i in iters:
    ...     print (i)
    ...
    <member 'name' of 'Dog' objects>
    <member 'weight' of 'Dog' objects>
    <member 'owner' of 'Dog' objects>
    ##如何解释？？？？
  

    >>> iters=Dog.__iter__(rex)
    >>> iters
    <generator object record_factory.<locals>.__iter__ at 0x01752C60>
    >>> for i in iters:
    ...     print (i)
    ...
    rex
    15
    jessie
    >>>
    
    ##iter(dog)事实上是调用了dog.__class__.__iter__(dog),因而改变dog的__iter__属性，并不会影响iter(dog)的调用
    '''