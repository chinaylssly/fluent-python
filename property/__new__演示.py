# _*_ coding:utf-8 _*_ 

class A(object):

    def __new__(cls,*args):

        return object.__new__(cls)

    def __init__(self,*args):

        print (u'init class A')



class B:

    def __new__(cls,*args):

        return super().__new__(A)

    def __init__(self,*args):

        print (u'init class B')



def test():


    a=A()
    b=B()
    print (a.__class__.__name__)
    print (b.__class__.__name__)
    b.__init__()


print (u'''我们通常把__init__称为构造方法，这是从其他语言借鉴来的术语。其实用于构造实例的特殊方法是__new__，
这是一个类方法，（做特殊处理，因此不必使用@metaclass装饰器），必须返回一个实例。返回的参数会作为第一个参数（即self），
传给__init__方法。因为调用 __init__方法时要传入一个实例，而且禁止返回任何值。所以__init__方法其实是初始化方法，
真正的构造方式是__new__，__new__方法也可以返回其他类的实例，此时解释器不会调用__init__方法。
        ''')
if __name__ == '__main__':

    test()

    '''
    >>> a=A()
    init class A
    >>> b=B()
    >>> a.__class__.__name__
    'A'
    >>> b.__class__.__name__
    'A'
    >>> b.__init__
    <bound method A.__init__ of <new1.A object at 0x01B61550>>
    >>> b.__init__()
    init class A
    '''

    print (u'B的__new__方法返回了A的实例，因而不会自动调用__init__方法，b手动调用的__init__方式是A的__init__方法')
