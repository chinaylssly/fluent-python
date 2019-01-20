# _*_ coding:utf-8 _*_ 

def quantity():
    
    try:
        quantity.counter +=1
    except AttributeError:
        quantity.counter=0

    storage_name='_{}#{}'.format('Quantity',quantity.counter)


    def get_attr(instance,):

        return getattr(instance,storage_name)
      
    def set_attr(instance,value):

        if value>0:
            setattr(instance,storage_name,value)
        else:
            raise(u'value must > 0,but get %s'%(value))

    return property(fget=get_attr,fset=set_attr)

class LineItem(object):

    weight=quantity()
    price=quantity()
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

    print (LineItem.weight,LineItem.price)


print (u'特性工厂函数模式简单，可是描述符类方式更易扩展，而且应用更广泛')

if __name__ =='__main__':

    test()

