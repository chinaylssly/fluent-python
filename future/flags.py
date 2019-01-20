# -*- coding: utf-8 -*-

import random,sys
from time import sleep,time


tl=[i*0.01 for i in range(20)]

def do_one(t=0.2):
    sleep(t)

def do_many(tl=tl):

    for t in tl:
        do_one(t)

    return len(tl)

def  main(do_many=do_many):

    t0=time()
    count=do_many()
    t=time()-t0
    msg='execute {:2d} task cost {:.2f} s'
    print (msg.format(count,t))

if __name__ =='__main__':
    main()






