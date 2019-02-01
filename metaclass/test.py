# _*_ coding:utf-8 _*_ 

def foo(d1,d2,d3=3,d4=4,*args,**kw):
    pass


for attr in (set(dir(foo)) - set(dir(object))):
    print (attr)
    print (getattr(foo,attr))
    print ()


code=getattr(foo,'__code__')
print (dir(code))

for attr in (set(dir(code)) - set(dir(object))):
    print (attr,getattr(code,attr))


from inspect import signature

sig=signature(foo)
# help(sig)
print (str(sig))

for name,param in sig.parameters.items():

    print (param.kind,':',name,'=',param.default)


