# _*_ coding:utf-8 _*_ 

class Quantity:
    
    __count=0

    ##__count是Quantity的类属性，统计Quantity类的实例数量

    def __init__(self,):

        cls=self.__class__
        #cls是Quantity类的引用

        prefix=cls.__name__

        self.storage_name=u'_%s#%d'%(prefix,cls.__count)
        ##每个描述符实例的storage_name都是独一无二的，因为其值由描述符类的名称和__count属性的当前值构成（如_Quantity#0）
        ##在前缀中使用#号能避免storage_name与用户使用点号创建的属性冲突，因为instance._Quantity#1是无效的Python句法。
        ##但是，使用getattr和setattr函数可以使用这种“无效的”标识符获取和设置属性

        cls.__count+=1
        #递增

    def __get__(self,instance,owner):
        #我们要实现__get__方法，因为托管属性的名称与storage_name不同。稍后会说明owner参数

        cls=self.__class__
        if hasattr(cls,'isprint'):
            pass
        else:
            print (u'args,instance.__class__ is owner: {}'.format(instance.__class__ is owner))
            ##LineItem在实例化后，owner就是type(instance),未实例化时，instance是None

            setattr(cls,'isprint',1)

        return getattr(instance,self.storage_name)
        ##使用内置的getattr函数从instance中获取存储属性的值

    def __set__(self,instance,value):
        ##尝试为托管属性赋值时，会调用__set__方法。这里，self是描述符实例(即Lineitem.weight或LineItem.price)，instance是托管实例（LineItem实例），value是有设定的值


        if value>0:
            
            setattr(instance,self.storage_name,value)
            ##这里使用内置setattr为instance设置相应的属性值,不需要通过instance.__dict__[self.storage_name]=value来为托管属性设置属性了，
            ##可以理解为(self.storage_name已经不是weight的特性property了

        else:
            raise(u'value must > 0,but get %s'%(value))

class LineItem(object):

    weight=Quantity()
    price=Quantity()
    ##现在不用把托管属性的名称传给Quantity的构造方法。这是这一版的目标

    def __init__(self,weight,price):

        self.weight=weight
        self.price=price

def test():

    lineitem=LineItem(1,2)
    print (lineitem.weight,lineitem.price)

    lineitem.weight=6

    print (lineitem.weight,lineitem.price)
    print (getattr(lineitem,'_Quantity#0'),getattr(lineitem,'_Quantity#1'))
    print (lineitem.__dict__['_Quantity#0'],lineitem.__dict__['_Quantity#1'])



print (u'''
注意，__get__方法有三个参数，self,instance,owner，owner参数是托管类（如Lineitem）的引用，通过描述符从托管类中获取属性时用得到。
如果使用LineItem.weight从类中获取托管属性，描述符的__get__方法接收到的instance参数值是None。因此，下面的控制台会话会抛出AttributeError异常：

>>> LineItem.weight
args,instance.__class__ is owner: False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:/Users/sunzhiming/Desktop/descriptor/LineItem_descriptor2.py", line 34, in __get__
    return getattr(instance,self.storage_name)
AttributeError: 'NoneType' object has no attribute '_Quantity#0'
>>>

抛出AttributeError异常是实现__get__方法的方式之一，如果选择这么做，应该修改错误消息，去掉令人困惑的NoneType和_Quantity#0,这是实现细节。
把错误消息改成"LineItem class has no such attribute更好"。最好能给出缺少的属性名，但在这个示例中，描述符并不知道托管属性的名称，因此目前只能做到这样。

此外，为了给用户提供内省和其他元编程技术，通过类访问托管属性时，最好让__get__方法返回描述符实例

    ''')
if __name__ =='__main__':

    test()

