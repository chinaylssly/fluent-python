import abc
import collections


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

# BEGIN MODEL_V8
class EntityMeta(type):
    """Metaclass for business entities with validated fields"""

    @classmethod
    def __prepare__(cls, name, bases):
        ##__prepare__方法的第一个参数是元类，随后的两个参数分别是要构建的类的名称和基类组成的元祖，返回值必须是映射。

        return collections.OrderedDict()  # <1>
        #返回一个空的OrderDict实例，类属性将存储在里面

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []  # <2>
        #在创建的类里创建一个_field_name属性

        for key, attr in attr_dict.items():  # <3>
        #这里的attr_dict是哪个OrderDict对象，由解释器在调用__init__方法之前调用__prepare__方法时获得。因此for循环会按照添加属性的顺序迭代属性

            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key)  # <4>
                #把找到的各个Validated字段添加到_field_names属性中


class Entity(metaclass=EntityMeta):
    """Business entity with validated fields"""

    @classmethod
    def field_names(cls):  # <5>
        for name in cls._field_names:
            yield name

# END MODEL_V8

'''
元类构建新类时，__prepare__方法的返回值会传给__new__方法的最后一个参数，然后在传给__init__方法。


'''