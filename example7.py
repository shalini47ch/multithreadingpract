#here we will use the concept of locks to solve this 
from threading import *
from time import sleep

mylock=Lock()

def task(mylock,msg):
    #put the acquire and the release functions so that you can lock the delicate code
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    mylock.release()
#now the next step is to create two threads

t1=Thread(target=task,args=(mylock,"hello world"))
t2=Thread(target=task,args=(mylock,"welcome"))
t1.start()
t2.start() 
#so by using the acquire and the release lock we are able to make them in a synchronised format
#when a thread is already released you cant release it multiple times 
#so multiple times lock and release karna possible nai hai 
#isko overcome karne ke liye abhi to rlock mechanism use kiya hua hai

    

