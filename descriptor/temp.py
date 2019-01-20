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

if __name__ =='__main__':

    test()

