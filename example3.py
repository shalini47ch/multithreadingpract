#here we will create threads for methods 

from threading import Thread

class Example:
    def display(self,n):
        for i in range(n):
            print("hello")
#here we will first create a thread
e1=Example()
t1=Thread(target=e1.display,args=(5,)) #the display function is created by the t1 thread
t1.start()

#this is the part which is being executed by the main thread
for i in range(4):
    print("world")


#there is no specific order that needs to be followed
