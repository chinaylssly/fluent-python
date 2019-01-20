# _*_ coding:utf-8 _*_

import LineItem_descriptor3  as model

class LineItem:

    weight = model.Quantity()
    price  = model.Quantity()
    descriptor=model.NonBlank()

    def __init__(self,weight,price,descriptor):

        self.weight=weight
        self.price=price
        self.descriptor=descriptor

    def __str__(self,):

        return'{}(weight:{},price:{},descriptor:{})'.format(self.__class__.__name__,self.weight,self.price,self.descriptor)



def test():

    print (LineItem(1,3,'apple'))
    # print (LineItem(-1,2,''))
print (u'本章所举的几个LineItem例子演示了描述符的典型用途--管理数据属性。这种描述符也叫覆盖型描述符，')
print (u'因为描述符的__set__方法使用托管实例中的同名属性覆盖（即插手接管）了要设置的属性。不过也有非覆盖型描述符 ')
if __name__ =='__main__':

    test()

