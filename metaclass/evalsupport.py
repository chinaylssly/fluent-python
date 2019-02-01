print('<[100]> evalsupport module start')

def deco_alpha(cls):
    print('<[200]> deco_alpha')

    def inner_1(self):
        print('<[300]> deco_alpha:inner_1')

    cls.method_y = inner_1
    return cls


class MetaAleph(type):

    print('<[400]> MetaAleph body')

    def __init__(cls, name, bases, dic):
        #编写元类时，通常会把self参数改成cls，能清楚表明要构建的实例是类

        print('<[500]> MetaAleph.__init__')

        def inner_2(self):
            print('<[600]> MetaAleph.__init__:inner_2')


        cls.method_z = inner_2

'''
__init__方法的定义体中定义了inner_2函数，然后将其绑定给了cls.method_z。MetaAleph.__init__方法签名中的cls指代要创建的类（例如ClassFive）。
而inner_2函数签名中的self最终是指代我们创建的类的实例（例如ClassFive类的实例）
'''

print('<[700]> evalsupport module end')
