# _*_ coding:utf-8 _*_ 

from decroptorkinds import Managed


print (u'在类中定义的函数属于绑定方法（bound method），因为用户定义的函数都有__get__方法，所以依附到类上时，就相当于描述符')

>>> obj=Managed()
>>> obj.spam
obj.spam获取的是绑定方法对象

<bound method Managed.spam of <descriptorkinds.Managed object at 0x01701110>>
>>> Managed.spam
<function Managed.spam at 0x017039C0>
Managed.spam获取的是函数

>>> obj.spam=5
如果为obj.spam赋值，会遮盖类属性，导致无法通过obj实例访问spam方法，所以函数可以看做是只实现了__get__方法的非覆盖型描述符。

>>> obj.spam
5


print (u'''

从上例可以看到一个重要信息：obj.spam 和 Managed.spam获取的是不同的对象。与描述符一样，通过托管类访问时，函数的__get__方法会返回函数自身的引用。
但是，通过实例访问时，函数的__get__返回的是绑定方法对象：一种可调用对象，里面包装着函数，并把托管实例（如obj）绑定给函数的第一个参数（即self），
这与functions.partial函数的行为一致。

函数会变成绑定方法，这是python语言底层使用描述符的最好例证

''')