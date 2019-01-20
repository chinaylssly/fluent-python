# _*_ coding:utf-8 _*_ 

from decroptorkinds import Managed




>>> obj.over_no_get
<descriptorkinds.OverridingNoGet object at 0x01725D70>
这个描述符没有__get__方法，因此，obj.over_no_get从类中获取描述符实例


>>> Managed.over_no_get
<descriptorkinds.OverridingNoGet object at 0x01725D70>
直接从托管类读取描述符实例也是如此

>>> obj.over_no_get=7
-> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
为obj.over_no_set赋值会触发描述符的__set__方法

>>> obj.over_no_get
<descriptorkinds.OverridingNoGet object at 0x01725D70>
因为__set__方法没有修改属性，所以在此读取obj.over_no_get获取的仍是托管类中描述符实例

>>> obj.__dict__['over_no_get']=8
通过obj实例的__dict__属性设置名为over_no_get的实例属性

>>> obj.over_no_get
8
现在，over_no_get实例属性会遮盖描述符，但是只有读操作如此

>>> obj.over_no_get=7
-> OverridingNoGet.__set__(<OverridingNoGet object>, <Managed object>, 7)
为obj.over_no_get赋值，仍然会经过描述符的__set__方法处理

>>> obj.over_no_get
8
>>>



