# _*_ coding:utf-8 _*_ 

from decroptorkinds import Managed



print (u'实现了__set__方法的描述符属于覆盖型描述符。特性property也是覆盖型描述符，\
    如果没有提供设值函数，property类的__set__会抛出AttributeErro异常')

'''
>>> obj=Managed()
>>> obj.over 
-> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
 ##obj.over触发描述符的__get__方法，第二个参数的值是托管实例obj

>>> Managed.over
-> Overriding.__get__(<Overriding object>, None, <class Managed>)
##Managed.over触发描述符的__get__方法，第二个参数是None

>>> obj.over=7
-> Overriding.__set__(<Overriding object>, <Managed object>, 7)
##obj.over=7，触发描述符的__set__方法，

>>> vars(obj)
{}
##之前obj.over=7,并没有改变obj.__dict__，因为描述符的__set__并没有向obj.__dict__插入新属性

>>> obj.__dict__['over']=8
>>> vars(obj)
{'over': 8}
##越过描述符，之间向obj.__dict__添加相应的键值对

>>> obj.over
-> Overriding.__get__(<Overriding object>, <Managed object>, <class Managed>)
##obj.over被描述符拦截了，调用了obj.__get__方法

>>> Managed.over=1000
>>> obj.over
8
##Managed的over属性被覆盖了，不再是特性（描述符），因而直接从obj.__dict__获取over属性的值
>>>

'''


