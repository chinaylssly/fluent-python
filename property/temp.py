# _*_ coding:utf-8 _*_ 

from traceback import print_exc
def prop(attr):

    def set_attr(instance,value):

        if value >0 :
            print ('set {}.{}={}'.format(instance.__class__.__name__,attr,value))
            instance.__dict__[attr]=value

        else:
            raise ValueError(u'{}.{} must be > 0,but get {}'.format(instance,attr,value))

    def get_attr(instance,):
        print (u'try get {}.{} from property get_attr'.format(instance,attr))
        return instance.__dict__[attr]


    def del_attr(instance,):

        print (u'delete {}.{}'.format(instance,attr))
        del instance.__dict__[attr]


    return property(fget=get_attr,fset=set_attr,fdel=del_attr,doc='set property from function prop')


class ItemLine:

    weight=prop('weight')
    price=prop('price')


    def __init__(self,weight,price,descriptor):

        self.weight=weight
        self.price=price
        self.descriptor=descriptor


    def __str__(self,):
        ##便于调试

        return u'ItemLine instance: weight=%s,price=%s'%(self.__dict__['weight'],self.__dict__['price'])





def test():

    print (ItemLine)
    print (ItemLine(1,2,1))
    print (ItemLine.weight.__doc__)

    try :
        itemline=ItemLine(-1,23,3)
    except ValueError as e:

        print (u'catch ValueError')
        print (e)
        print_exc()

    except KeyError as e:
        ##捕捉到了KeyError，而非ValueError

        print (u'catch KeyError')
        print (e)
        print_exc()

if __name__ =='__main__':
    
    test()


    '''

    <class '__main__.ItemLine'>
    set ItemLine.weight=1
    set ItemLine.price=2
    ItemLine instance: weight=1,price=2
    set property from function prop

    

    catch KeyError
    'weight'
    Traceback (most recent call last):
      File "C:\Users\sunzhiming\Desktop\meta\temp.py", line 58, in test
        itemline=ItemLine(-1,23,3)
      File "C:\Users\sunzhiming\Desktop\meta\temp.py", line 37, in __init__
        self.weight=weight
      File "C:\Users\sunzhiming\Desktop\meta\temp.py", line 13, in set_attr
        raise ValueError(u'{}.{} must be > 0,but get {}'.format(instance,attr,value))
      File "C:\Users\sunzhiming\Desktop\meta\temp.py", line 45, in __str__
        return u'ItemLine instance: weight=%s,price=%s'%(self.__dict__['weight'],self.__dict__['price'])
    KeyError: 'weight'

    '''