# _*_ coding:utf-8 _*_ 

from decroptorkinds import Managed


print (u'若想控制设置类属性的操作，要把描述符依附在类的类上，即依附在元类上。默认情况下，对用户定义的类来说，其元类是type，而我们不能为元类添加属性')

>>> obj=Managed()
>>> Managed.over=1
>>> Managed.over_no_get=2
>>> Managed.non_over=3
覆盖类中的描述符属性

>>> obj.over,obj.over_no_get,obj.non_over
(1, 2, 3)
描述符不见了
>>>

print (u'上例揭示了读写属性的另一种不对等；读 类属性的操作可以 依附在 托管类上 定义有__get__方法的描述符处理')
print (u'但是写 类属性的操作不会由 依附在托管类上定义有__set__方法的描述符处理')

print (u'因为__get__方法的第二个参数instance传入None的时候，代表要获取的是类属性，而__set__的instance参数貌似不能代表类本身（也没必要代表）')