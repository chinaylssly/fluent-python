# _*_ coding:utf-8 _*_ 

class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):  # <1>
        ##普通的读值方法

        return self.__weight

    def set_weight(self, value):  # <2>
        ##普通的设值方法

        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

    weight = property(get_weight, set_weight)  # <3>
    ##构建property对象，然后赋值给公开的类属性

print (u'类中的特性能影响实例属性的寻找方式。')    
