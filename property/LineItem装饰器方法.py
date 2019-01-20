# _*_ coding:utf-8 _*_ 

class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        #实现特性的方法，其名称都与公开属性的名称一样--weight

        return self.__weight
        #真正的值保存在私有属性__weight


    @weight.setter
    def weight(self,value):
        if value>0:
            self.__weight=value

        else:
            raise ValueError('value must be > 0')



'''
Tips:

引用Paul Graham 的一句话，他说：“当我在自己的程序中发现用到了模式，我觉得这就表明某个地方出错了”，去除重复的方法就是抽象。

抽象特性的定义有两种方式：使用特性工厂函数，或者使用描述符类。后者更灵活
'''
