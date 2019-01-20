# -*- coding: utf-8 -*-
import threading
import itertools
import time
import sys


class Signal:
    ##一个简单的可变对象，从外部控制线程
    go=True


def spin(msg,signal):
    write,flush = sys.stdout.write,sys.stdout.flush

    ##itertools.cycle函数会从制定的序列中反复不断地生成元素
    for char in itertools.cycle('|/-\\'):
        status=char + ' ' + msg
        write(status)
        flush()

        ##这是显示动画的诀窍，使用退格符\x08将光标移回来
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    ##使用空格清除状态消息，吧光标移回开头
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():

    time.sleep(10)
    return 42


def supervisor():

    signal=Signal()
    spinner=threading.Thread(target=spin,args=('thinking',signal))

    print ('spinner object before start:',spinner)
    spinner.start()

    print ('spinner object after start:',spinner)

    ##slow_function函数会阻塞主线程。同时从属线程会以动画形式显示旋转指针
    result=slow_function()

    signal.go=False

    print ('spinner object after set False:',spinner)

    time.sleep(1)
    ##发送False消息后，spinner线程stoped，sleep 1 秒是由于等待spinner线程执行到break所在的条件判断语句
    print ('spinner object after sleep:',spinner)

    spinner.join()

    print ('spinner object after join:',spinner)
    return result


def main():

    result=supervisor()
    print ('Answer: ',result)


print (u'python中没有提供终止线程的API，这是有意为之。若想关闭线程，必须给线程发送消息')
print (u'本程序中，使用signal.go属性，在主线程中将它设为False后，spinner线程最终会注意到，然后干净的退出')

if __name__ =='__main__':

    main()


    '''
    >>> main()
    spinner object before start: <Thread(Thread-1, initial)>
    | thinkingspinner object after start: <Thread(Thread-1, started 6692)>
    spinner object after set False: <Thread(Thread-1, started 6692)>
    spinner object after sleep: <Thread(Thread-1, stopped 6692)>
    spinner object after join: <Thread(Thread-1, stopped 6692)>
    Answer:  42

    '''