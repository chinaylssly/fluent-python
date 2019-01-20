# _*_ coding:utf-8 _*_ 

class LineItem:

    def __init__(self,weight,price,descriptor):

        self.weight=weight
        self.price=price
        self.descriptor=descriptor

    def set_weight(self,value):

        if value > 0:
            print ('set weight:{:3d}'.format(value))
            self.__dict__['weight']=value

        else:

            raise ValueError(u'weight must be >0, but get {:3d}'.format(value))

    def get_weight(self,):

        return self.__dict__['weight']


    def __str__(self,):

        return '<{}.weight={:3d},{}.price={:3d}>'.format(self.__class__.__name__,self.weight,self.__class__.__name__,self.price)



    weight=property(get_weight,set_weight)


def test():

    print (LineItem(weight=3,price=5,descriptor=u''))
    try:
        print (LineItem(weight=-3,price=5,descriptor=u''))
    except ValueError as e:
        print (u'catch ValueError')
        print (e)

    import inspect



if __name__ =='__main__':

    test()
