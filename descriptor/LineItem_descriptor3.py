# _*_ coding:utf-8 _*_ 

import abc

class AUtoStorage:
    ##提供之前Quantity描述符的大部分功能，验证除外

    __counter=0

    def __init__(self,):

        cls=self.__class__
        prefix=cls.__name__
        index=cls.__counter
        self.storage_name=u'_{}#{}'.format(prefix,index)
        cls.__counter+=1

    def __get__(self,instance,owner):

        if instance is None:
            return self
        else:
            return getattr(instance,self.storage_name)

    def __set__(self,instance,value):

        setattr(instance,self.storage_name,value)

class Validated(abc.ABC,AUtoStorage):
    ##Validated是抽象类，不过也继承自AutoStorage类(为什么不把AutoStorage直接并入这里呢)

    def __set__(self,instance,value):
        ##__set__方法把验证操作委托给validate方法

        value=self.validate(instance,value)
        ##把返回的值传给超类的__set__方法，存储值

        super().__set__(instance,value)

    @abc.abstractmethod
    def validate(self,instance,value):
        #在这个类中，validate是抽象方法
        '''return validated value or raise ValueError'''

class Quantity(Validated):
    '''a num greater than zero'''
    #Quantity和NonBlank类都继承自Validated类，需要实现父类的抽象方法

    def validate(self,instance,value):

        if value <0:
            raise ValueError(u'Value must be > 0')
        return value

class NonBlank(Validated):

    def validate(self,instance,value):
        '''a string with at least one non-space character'''
        value=value.strip()
        if len(value) ==0:
            raise ValueError(u'Value cannot be empty or blank')
        else:
            return value




