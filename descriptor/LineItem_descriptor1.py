# _*_ coding:utf-8 _*_ 

class Quantity:
    ##描述符基于协议实现，无需创建子类（无需继承自别的类）

    def __init__(self,storage_name):

        self.storage_name=storage_name
        #Quantity实例有个storage_name属性,这是托管实例中存储值的属性的名称

    def __set__(self,instance,value):
        ##尝试为托管属性赋值时，会调用__set__方法。这里，self是描述符实例(即Lineitem.weight或LineItem.price)，instance是托管实例（LineItem实例），value是有设定的值

        if value>0:
            #这里必须直接处理托管实例的__dict__属性，如果使用内置的setattr函数，会在此触发__set__方法，导致无限递归
            instance.__dict__[self.storage_name]=value

        else:
            raise(u'value must > 0,but get %s'%(value))

class LineItem(object):

    weight=Quantity('weight')
    price=Quantity('price')

    def __init__(self,weight,price):

        self.weight=weight
        self.price=price

def test():

    lineitem=LineItem(1,2)
    print (lineitem.weight,lineitem.price)

    lineitem.weight=6
    #quantity描述符不需要实现__get__方法就能修改属性的值，这是与property不一样的地方,因为其默认调用了__getattribute__方法

    print (lineitem.weight,lineitem.price)


print (u'这个ItemLine还有一个缺点，在托管类的定义体中实例化描述符要重复输入属性的名称。如weight=Quantity("weight")')
print (u'如果能向下面一样声明就好了,weight=Quantity()')

if __name__ =='__main__':

    test()

