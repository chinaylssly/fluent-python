# _*_ coding:utf-8 _*_ 



'''
Tips:
property经常用作装饰器，但其实他是一个类。
property构造方法的完整签名如下：
property(fget=None,fset=None,fdel=None,doc=name)
所有参数都是可选的，如果没有把函数传给某个参数，那么得到的特性对象就不允许执行相应的操作

'''
class Class:

    data='the class data attr'

    @property
    def prop(self):
        return 'the prop value'


def test_Class():

    obj=Class()
    print (vars(obj))
    #vars(obj) <=> obj.__dict__

    print (obj.data)
    obj.data='bar'
    ##只有赋值方法能往实例的__dict__中添加属性，只是调用该属性并不能改变实例的__dict__

    print (vars(obj))
    print (Class.data)

    print ('\n')

    print (Class.prop)
    print (obj.prop)
    try:
        obj.prop='foo'
        #不能设置只读属性

    except Exception as e:
        print (e)
        print (e.__traceback__.tb_frame.f_code.co_varnames)

    obj.__dict__['prop']='foo'
    #可以直接把'prop'存入obj.__dict__

    print (vars(obj))
    #可以看到vars(obj)有两个属性

    print (obj.prop)
    #然而，读取obj.prop时仍会运行特性的读值方式。特性没被实例属性遮盖

    Class.prop='baz'
    #覆盖Class.prop特性，销毁特性对象

    print (obj.prop)
    #现在obj.prop获取的是实例属性。Class.prop不再是特性了，因此不会再覆盖obj.prop。


    Class.data=property(lambda self: 'the "data" prop value')
    #是用特性覆盖Class.data

    print (obj.data)
    #obj.data被Class.data特性遮盖了。

    del Class.data
    #删除特性

    print (obj.data)
    #现在恢复原样，obj.data获取的是实例属性data

print (u'obj.attr这样的表达式不会从obj开始寻找attr，而是从obj.__class__开始，而且，仅当类中没有attr的特性时，python才会在obj的实例中寻找。')
print (u'这条规则不仅适用于特性，还适用于一整类描述符--覆盖型描述符（overriding descriptor）。特性其实是覆盖型描述符')
print (u'特性是个强大的功能，不过有时更适合使用简单的或底层的替代方案')

if __name__=='__main__':

    test_Class()


    '''
    >>> obj=Class()
    >>> vars(obj)
    {}
    >>> obj.data
    'the class data attr'
    >>> vars(obj)
    {}
    >>> obj.data='bar'
    >>> vars(obj)
    {'data': 'bar'}
    >>> obj.data
    'bar'
    >>> Class.data
    'the class data attr'
    
    ##以上为类的普通属性

   
    >>> Class.prop
    <property object at 0x018D34B0>
    >>> obj.prop
    'the prop value'
    >>> obj.prop ='foo'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
    >>> obj.__dict__['prop']='foo'
    >>> vars(obj)
    {'data': 'bar', 'prop': 'foo'}
    >>> obj.prop
    'the prop value'
    >>> Class.prop='baz'
    >>> obj.prop
    'foo'



    >>> Class.data=property(lambda self: 'the "data" prop value')
    >>> obj.data
    'the "data" prop value'
    >>> del Class.data
    >>> vars(obj)
    {'data': 'bar', 'prop': 'foo'}
    >>> obj.data
    'bar'
    >>>

    '''

    
