import abc

class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""


class Quantity(Validated):
    """a number greater than zero"""

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value


class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value

# BEGIN MODEL_V6
def entity(cls):  # <1>
    #类装饰器的参数是一个类

    for key, attr in cls.__dict__.items():  # <2>
    #迭代存储类属性的字典

        if isinstance(attr, Validated):  # <3>
        #如果属性是Validated描述符的实例。（这里可以看出对类进行抽象，然后继承的好处，可以把不同的子类实例判断是否为父类的实例）

            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)  # <4>
            #使用描述符的名称和托管属性的名称命名storage_name(例如_Nonblank#description)。

    return cls  # <5>
    #返回修改后的类

# END MODEL_V6


def test():
    pass


print (u'类的装饰器能以较简单的方式做到以前需要使用元类去做的事情--创建类时定制类')
print (u'类装饰器有个重大缺点：只对直接依附的类有效。这意味着，被装饰类的子类可能继承也可能不继承类装饰器所做的改动，具体情况视改动的方式而定')

if __name__=='__main__':

    test()

    '''
    
    >>> from LineItem_class_descriptor import LineItem
    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins
    <LineItem_class_descriptor.LineItem object at 0x017555B0>

    >>> raisins.__dict__
    {'_NonBlank#description': 'Golden raisins', '_Quantity#weight': 10, '_Quantity#price': 6.95}
    >>> vars(raisins)
    {'_NonBlank#description': 'Golden raisins', '_Quantity#weight': 10, '_Quantity#price': 6.95}
  

    >>> LineItem.description.storage_name
    '_NonBlank#description'

    >>> raisins.description
    'Golden raisins'

    >>> getattr(raisins,'_NonBlank#description')
    'Golden raisins'

    >>> getattr(raisins,'description')
    'Golden raisins'

>>>



    
    '''
