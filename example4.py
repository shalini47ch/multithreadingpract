#to find out the names of the threads we will be using  the .name method from threading 
from threading import Thread

def display():
    for i in range(4):
        print("hello world")
#we will create one thread for the display function and the other thread for the show function

def show():
    for i in range(2):
        print("welcome")

#creating threads for these two functions 
t1=Thread(target=display)
t2=Thread(target=show)
# print(t1.name)
# print(t2.name)
t1.start()
t2.start()
#there are two types of identifiers in case of threads one is the thread identifier and the other is the native identifier
#thread identifier has an id of ident, and nativeidentifier has an id of native_id
print("***",t1.ident)
print("+++",t1.native_id) #these will have the same values but they are different ids



