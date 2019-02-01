# _*_ coding:utf-8 _*_ 
import abc

class AutoStorage:

    __count=0
    def __init__(self,):
        cls=self.__class__
        self.strorage_name=u'_{}#{}'.format(cls.__name__,cls.__count)
        ##带__的属性，在类内部访问时不需要修改为_cls__attr的形式
        cls.__count+=1

    def __set__(self,instance,value):

        setattr(instance,self.strorage_name,value)

    def __get__(self,instance,owner):

        if instance is None:
            return self
        else:
            return getattr(instance,self.strorage_name)


class Validated(abc.ABC,AutoStorage):

    def __set__(self,instance,value):
        ##这么看，AutoStorage没必要实现具体的__set__方法，也可以抽象了！

        value=self.validate(value)
        super().__set__(instance,value)

 
    @abc.abstractmethod
    def validate(self,value):
        '''检查赋值是否有效，抽象方法'''





class Quantity(Validated):
    ##检查变量是否大于0

    def validate(self,value):
        if value>0:
            return value
        else:
            raise ValueError(u'value must >0')

class NonBlank(Validated):
    ##检查设置的值是否为空

    def validate(self,value):

        value=value.strip()

        if len(value)==0:

            raise ValueError(u'Vvalue cannot be empty or blank')

        else:

            return value


def entity(cls):
    ##用作类装饰器，修改托管属性描述符实例的storage_name的值

    for key,value in cls.__dict__.items():

        if isinstance(value,Validated):

            strorage_name=u'_{}#{}'.format(value.__class__.__name__,key)
            value.strorage_name=strorage_name

    return cls


@entity
class LineItem:

    description=NonBlank()
    weight=Quantity()
    price=Quantity()

    def __init__(self,weight,price,description):

        self.description=description
        self.price=price
        self.weight=weight

    def __repr__(self,):

        return u', '.join('{}:{}'.format(*item) for item in self.__dict__.items())



def test():

    line=LineItem(5,12,'Apple')
    print (line)

    print (line.weight,line.price,line.description)

    print (getattr(line,'weight'))
    print (getattr(line,'_Quantity#weight'))


if __name__ =='__main__':

    test()







