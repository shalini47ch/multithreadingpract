#here we need to create threads in python
#this is one way to create threads in python

from threading import Thread,current_thread

def display(n,msg):
    print(current_thread())
    for i in range(n):
        print(msg)

t1=Thread(target=display,args=(4,"Hello"))
t1.start()
#if we want to see the details of the t1 thread we can use the current_thread method
