# -*- coding: utf-8 -*-
import time



class LookingGlass(object):
    '''
    上下文管理器需要实现 __entry__ 和 __exit__ 方法
    '''
    def __enter__(self,):
        import sys
        self.original_write=sys.stdout.write
        sys.stdout.write=self.reverse_write
        return 'JJAJJALALALA'

    def reverse_write(self,text):

        self.original_write(text[::-1])


    def __exit__(self,exc_type,exc_value,traceback):

        import sys
        sys.stdout.write=self.original_write
        if exc_type is ZeroDivisionError:
            print (u'please DO NOT divide by zero')
            return True



with LookingGlass() as what:
    print (u'你好，python')
    print (what)
    # a=5/0
    b=5/10
    print (112)
print (what)