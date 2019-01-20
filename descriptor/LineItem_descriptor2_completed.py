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

        if instance is None:
            return self
            ##不是通过实例调用，返回其本身
        else:
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

你可能觉得为了管理几个属性而编写这么多代码不值得，但是要知道，描述符逻辑被抽象到了单独的代码单元（Quantity类）中了。
通常，我们不会在使用描述符的模块中定义描述符，而是在一个单独的实用工具中定义，以便在整个应用中使用，如果开发的是框架，甚至会在多个应用中使用。
Django的ORM模型的字段就是描述符

    ''')
if __name__ =='__main__':

    test()

