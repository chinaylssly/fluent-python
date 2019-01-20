# _*_ coding:utf-8 _*_ 

def quantity(storage_name):  # <1>
    ##storage_name参数确定各个特性的数据存储在哪儿，对weight特性来说，存储的名称是'weight'

    def qty_getter(instance):  # <2>
        #qty_getter的第一个参数可以命名为self，但是这么做很奇怪，因为qty_setter函数不在类定义体内，instance指代要把属性存储其中的LineItem实例

        return instance.__dict__[storage_name]  # <3>
         #qty_getter引用了storage_name，把它保存在这个函数的闭包里；值直接从instance.__dict__中获取，为的是跳过特性，防止无限递归。

        #return instance.storage_name
        #return instance.storage_name的话，就会接着调用qty_getter,会造成无限递归，同理qty_setter一样

    def qty_setter(instance, value):  # <4>
        #定义qty_setter函数，第一个参数也是instance

        if value > 0:
            instance.__dict__[storage_name] = value  # <5>
            ##值直接存储到instance.__dict__中，这也是为了跳过特性。
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)  # <6>
    ##构建一个自定义特性对象，然后将其返回



class LineItem:
    weight = quantity('weight')  # <1>
    ##使用工厂函数，把自定义的特性weight定义为类属性

    price = quantity('price')  # <2>
    ##类似于scrapy中的Field()

    print (u'特性是类属性，构建各个quantity特性对象时，要传入LineItem的实例属性的名称，让特性管理。可惜，这一行要两次输入单词weight')
    print (u'这里很难避免重复输入，因为特性根本不知道要绑定哪个类属性名。记住，赋值语句的右边先计算，因此调用quantity()时，weight类属性还不存在。')
    print (u'要想改变quantity特性，避免用户重复输入属性名，对元编程是一个挑战。后面会介绍变通方法，真正的解决方法，要么使用类装饰器，要么使用元类')


    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # <3>
        #特性已经被激活，确保不能把weight设为负数或零

        self.price = price

    def subtotal(self):
        return self.weight * self.price  # <4>
        ##使用特性获取实例中储存的值

    ##如果直接使用property装饰属性，那么每一个属性都需要property装饰，会导致大量的代码重复。not pythonc




def test():

    nutmeg=LineItem('Moluccan',8,13.95)

    print (nutmeg.weight,nutmeg.price)
    ##通过特性读取同名属性，会覆盖同名实例属性

    print (sorted(nutmeg.__dict__.items()))
    #使用__dict__社差nutmeg实例，查看真正用于储存值得实例属性


print (u'工厂函数构建的特性利用了weight特性覆盖实例属性的行为，因此对self.weight 或 nutmeg.weight的每个引用都由特性函数处理，只有直接存取__dict__属性才能跳过特性的处理逻辑')
print (u'真实处理场景中，分散在多个类中多个字段可能要做同样的验证，此时最好把quantity工厂函数放在工具模块里。')
print (u'最终也可能要重构工厂函数，改为更易扩展的描述符类，然后使用子类执行不同的验证')
print (u'PS:这一切都是为了避免代码重复，和可扩展性，可复用性，健壮性')

if __name__ =='__main__':

    test()

    '''
    >>nutmeg=LineItem('Moluccan',8,13.95)
    >>nutmeg.weight,nutmeg.price
    8 13.95
    >>
    sorted(nutmeg.__dict__.items())
    [('description', 'Moluccan'), ('price', 13.95), ('weight', 8)]
    '''


