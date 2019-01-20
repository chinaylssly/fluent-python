# _*_ coding:utf-8 _*_ 

from decroptorkinds import Managed


print (u'没有设置__set__方法的描述符是非覆盖型描述符。如果设置了同名的实例属性，描述符会被覆盖，致使描述符无法处理那个实例的属性')


>>> obj.non_over
-> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
obj.non_over出发了描述符的__get__方法，第二个参数的值是obj

>>> obj.non_over=7
Managed.non_over是非覆盖型描述符，因此，没有干涉赋值操作的__set__方法

>>> obj.non_over
7
现在，obj有个名为non_over的实例属性，把Managed类的同名描述符属性遮盖掉

>>> Managed.non_over
-> NonOverriding.__get__(<NonOverriding object>, None, <class Managed>)
Managed.non_over描述符依然存在，会通过类截取这次访问

>>> del obj.non_over
把obj.non_over实例属性删除

>>> obj.non_over
-> NonOverriding.__get__(<NonOverriding object>, <Managed object>, <class Managed>)
那么，读取obj.non_over时，会触发描述符的__get__方法，但要注意，第二个参数是托管实例obj

>>>


