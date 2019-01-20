# _*_ coding:utf-8 _*_ 

1，dir(object)
    
    返回对象的大多数属性

2，getattr(obj,name[,default])

    从obj对象获取name字符串对应的属性，获取的属性可能来自obj所属的类，或是超类

3，hasattr(obj,name)
    
    根据getattr是否抛出异常判断

4，setattr(obj,name,value)
    
    把obj对应的属性更改为value

5，vars(obj)

    返回obj的__dict__属性


a, __delattr__(self,name)
    
    只有使用del删除属性，就会调用这个方法。例如，del obj.attr语句触发 Class.__delattr__(obj,attr)

b，__dir__(self)
    
    把对象传给dir函数调用，例如:dir(obj)触发Class.__dir__(obj)方法


c, __getattr__(self,name):
    
    仅当获取指定的属性失败，搜索过obj、Class、和超类之后调用。表达式obj.no_such_attr、getattr(obj,'no_such_attr')、和hasattr(obj,'no_such_attr')可能会
    触发Class.__getattr__(obj,name),但是，仅当在obj、Class和超类中找不到指定属性时才触发。

d, __getattribute__(self,name)

    尝试获取指定的属性都会调用这个方法，不过，寻找的属性是特殊属性或特殊方法时除外。点号与getattr和hasattr内置函数会触发这个方法。调用__getattribute__方法且
    抛出AttributeError异常时，才会调用__getattr__方法。为了在获取obj的实例属性时不导致无限递归，__getattribute__方法的实现要使用super().__getattribute__(obj,anme).

e, __setattr__(self,name.value)

    尝试设置指定的属性时会调用这个方法，obj.attr=value 和 setattr(obj,attr,value)都会触发Class.__setattr__(obj,attr,value)


其实，特殊方法__getattribute__和__setattr__不管怎么调用，几乎都会影响属性的存取，因而比__getattr__方法（只处理不存在的属性名）更难正确使用。
与定义这些特殊方法相比，使用特性或描述符相对不易出错   

